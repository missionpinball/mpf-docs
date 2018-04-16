import tempfile

from pygments.lexer import include, bygroups
from pygments.token import Comment, String, Text, Punctuation, Number, Keyword, Name, Literal
from pygments.lexers.data import YamlLexer

class MpfLexer(YamlLexer):

    name = 'mpf-config'

    def nothing(token_class):
        """Do not produce empty tokens."""
        def callback(lexer, match, context):
            yield match.start(), token_class, ""
            context.pos = match.end()
        return callback

    tokens = {
        # the root rules
        'root': [
            # ignored whitespaces
            (r'[ ]+(?=#|$)', Text),
            # line breaks
            (r'\n+', Text),
            # doc ignore comment
            (r'#![^\n]*\n', nothing(Text)),
            (r'##![^\n]*\n', nothing(Text)),
            # a comment
            (r'#[^\n]*', Comment.Single),
            # the '%YAML' directive
            (r'^%YAML(?=[ ]|$)', YamlLexer.reset_indent(Name.Tag), 'yaml-directive'),
            # the %TAG directive
            (r'^%TAG(?=[ ]|$)', YamlLexer.reset_indent(Name.Tag), 'tag-directive'),
            # document start and document end indicators
            (r'^(?:---|\.\.\.)(?=[ ]|$)', YamlLexer.reset_indent(Name.Namespace),
             'block-line'),
            # indentation spaces
            (r'[ ]*(?!\s|$)', YamlLexer.save_indent(Text, start=True),
             ('block-line', 'indentation')),
        ],

        # trailing whitespaces after directives or a block scalar indicator
        'ignored-line': [
            (r'#[^\n]*', YamlLexer.something(Text)),
            # ignored whitespaces
            (r'[ ]+(?=#|$)', Text),
            # a comment
            (r'#[^\n]*', Comment.Single),
            # line break
            (r'\n', Text, '#pop:2'),
        ],

        # the %YAML directive
        'yaml-directive': [
            # the version number
            (r'([ ]+)([0-9]+\.[0-9]+)',
             bygroups(Text, Number), 'ignored-line'),
        ],

        # the %YAG directive
        'tag-directive': [
            # a tag handle and the corresponding prefix
            (r'([ ]+)(!|![\w-]*!)'
             r'([ ]+)(!|!?[\w;/?:@&=+$,.!~*\'()\[\]%-]+)',
             bygroups(Text, Keyword.Type, Text, Keyword.Type),
             'ignored-line'),
        ],

        # block scalar indicators and indentation spaces
        'indentation': [
            # trailing whitespaces are ignored
            (r'[ ]*$', YamlLexer.something(Text), '#pop:2'),
            # whitespaces preceeding block collection indicators
            (r'[ ]+(?=[?:-](?:[ ]|$))', YamlLexer.save_indent(Text)),
            # block collection indicators
            (r'[?:-](?=[ ]|$)', YamlLexer.set_indent(Punctuation.Indicator)),
            # the beginning a block line
            (r'[ ]*', YamlLexer.save_indent(Text), '#pop'),
        ],

        # an indented line in the block context
        'block-line': [
            # the line end
            (r'[ ]*(?=#|$)', YamlLexer.something(Text), '#pop'),
            # whitespaces separating tokens
            (r'[ ]+', Text),
            # tags, anchors and aliases,
            include('descriptors'),
            # block collections and scalars
            include('block-nodes'),
            # flow collections and quoted scalars
            include('flow-nodes'),
            # a plain scalar
            (r'(?=[^\s?:,\[\]{}#&*!|>\'"%@`-]|[?:-]\S)',
             YamlLexer.something(Name.Variable),
             'plain-scalar-in-block-context'),
        ],

        # tags, anchors, aliases
        'descriptors': [
            # a full-form tag
            (r'!<[\w#;/?:@&=+$,.!~*\'()\[\]%-]+>', Keyword.Type),
            # a tag in the form '!', '!suffix' or '!handle!suffix'
            (r'!(?:[\w-]+!)?'
             r'[\w#;/?:@&=+$,.!~*\'()\[\]%-]+', Keyword.Type),
            # an anchor
            (r'&[\w-]+', Name.Label),
            # an alias
            (r'\*[\w-]+', Name.Variable),
        ],

        # block collections and scalars
        'block-nodes': [
            # implicit key
            (r':(?=[ ]|$)', YamlLexer.set_indent(Punctuation.Indicator, implicit=True)),
            # literal and folded scalars
            (r'[|>]', Punctuation.Indicator,
             ('block-scalar-content', 'block-scalar-header')),
        ],

        # flow collections and quoted scalars
        'flow-nodes': [
            # a flow sequence
            (r'\[', Punctuation.Indicator, 'flow-sequence'),
            # a flow mapping
            (r'\{', Punctuation.Indicator, 'flow-mapping'),
            # a single-quoted scalar
            (r'\'', String, 'single-quoted-scalar'),
            # a double-quoted scalar
            (r'\"', String, 'double-quoted-scalar'),
        ],

        # the content of a flow collection
        'flow-collection': [
            # whitespaces
            (r'[ ]+', Text),
            # line breaks
            (r'\n+', Text),
            # a comment
            (r'#[^\n]*', Comment.Single),
            # simple indicators
            (r'[?:,]', Punctuation.Indicator),
            # tags, anchors and aliases
            include('descriptors'),
            # nested collections and quoted scalars
            include('flow-nodes'),
            # a plain scalar
            (r'(?=[^\s?:,\[\]{}#&*!|>\'"%@`])',
             YamlLexer.something(Name.Variable),
             'plain-scalar-in-flow-context'),
        ],

        # a flow sequence indicated by '[' and ']'
        'flow-sequence': [
            # include flow collection rules
            include('flow-collection'),
            # the closing indicator
            (r'\]', Punctuation.Indicator, '#pop'),
        ],

        # a flow mapping indicated by '{' and '}'
        'flow-mapping': [
            # include flow collection rules
            include('flow-collection'),
            # the closing indicator
            (r'\}', Punctuation.Indicator, '#pop'),
        ],

        # block scalar lines
        'block-scalar-content': [
            # line break
            (r'\n', Text),
            # empty line
            (r'^[ ]+$',
             YamlLexer.parse_block_scalar_empty_line(Text, Name.Constant)),
            # indentation spaces (we may leave the state here)
            (r'^[ ]*', YamlLexer.parse_block_scalar_indent(Text)),
            # line content
            (r'[\S\t ]+', Name.Constant),
        ],

        # the content of a literal or folded scalar
        'block-scalar-header': [
            # indentation indicator followed by chomping flag
            (r'([1-9])?[+-]?(?=[ ]|$)',
             YamlLexer.set_block_scalar_indent(Punctuation.Indicator),
             'ignored-line'),
            # chomping flag followed by indentation indicator
            (r'[+-]?([1-9])?(?=[ ]|$)',
             YamlLexer.set_block_scalar_indent(Punctuation.Indicator),
             'ignored-line'),
        ],

        # ignored and regular whitespaces in quoted scalars
        'quoted-scalar-whitespaces': [
            # leading and trailing whitespaces are ignored
            (r'^[ ]+', Text),
            (r'[ ]+$', Text),
            # line breaks are ignored
            (r'\n+', Text),
            # other whitespaces are a part of the value
            (r'[ ]+', Name.Variable),
        ],

        # single-quoted scalars
        'single-quoted-scalar': [
            # include whitespace and line break rules
            include('quoted-scalar-whitespaces'),
            # escaping of the quote character
            (r'\'\'', String.Escape),
            # regular non-whitespace characters
            (r'[^\s\']+', String),
            # the closing quote
            (r'\'', String, '#pop'),
        ],

        # double-quoted scalars
        'double-quoted-scalar': [
            # include whitespace and line break rules
            include('quoted-scalar-whitespaces'),
            # escaping of special characters
            (r'\\[0abt\tn\nvfre "\\N_LP]', String),
            # escape codes
            (r'\\(?:x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})',
             String.Escape),
            # regular non-whitespace characters
            (r'[^\s"\\]+', String),
            # the closing quote
            (r'"', String, '#pop'),
        ],

        # the beginning of a new line while scanning a plain scalar
        'plain-scalar-in-block-context-new-line': [
            # empty lines
            (r'^[ ]+$', Text),
            # line breaks
            (r'\n+', Text),
            # document start and document end indicators
            (r'^(?=---|\.\.\.)', YamlLexer.something(Name.Namespace), '#pop:3'),
            # indentation spaces (we may leave the block line state here)
            (r'^[ ]*', YamlLexer.parse_plain_scalar_indent(Text), '#pop'),
        ],

        # a plain scalar in the block context
        'plain-scalar-in-block-context': [
            # the scalar ends with the ':' indicator
            (r'[ ]*(?=:[ ]|:$)', YamlLexer.something(Text), '#pop'),
            # the scalar ends with whitespaces followed by a comment
            (r'[ ]+(?=#)', Text, '#pop'),
            # trailing whitespaces are ignored
            (r'[ ]+$', Text),
            # line breaks are ignored
            (r'\n+', Text, 'plain-scalar-in-block-context-new-line'),
            # other whitespaces are a part of the value
            (r'[ ]+', Literal.Scalar.Plain),
            # regular non-whitespace characters
            (r'(?::(?!\s)|[^\s:])+', Literal.Scalar.Plain),
        ],

        # a plain scalar is the flow context
        'plain-scalar-in-flow-context': [
            # the scalar ends with an indicator character
            (r'[ ]*(?=[,:?\[\]{}])', YamlLexer.something(Text), '#pop'),
            # the scalar ends with a comment
            (r'[ ]+(?=#)', Text, '#pop'),
            # leading and trailing whitespaces are ignored
            (r'^[ ]+', Text),
            (r'[ ]+$', Text),
            # line breaks are ignored
            (r'\n+', Text),
            # other whitespaces are a part of the value
            (r'[ ]+', Name.Variable),
            # regular non-whitespace characters
            (r'[^\s,:?\[\]{}]+', Name.Variable),
        ],

    }

# this could be used to show some test output
#    def get_tokens_unprocessed(self, text=None, context=None):
#        value = super().get_tokens_unprocessed(text, context)
#        return value

