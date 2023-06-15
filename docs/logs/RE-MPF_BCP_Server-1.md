---
title: RE-MPF_BCP_Server-1: Failed to bind BCP Socket to 127.0.0.1 on
  port 5051
---

Related Config File Sections:

* [bcp:](../config/bcp.md)

This error occurs when MPF cannot bind the port 5051 for incoming BCP
connections. The same error can occur in MC when it cannot bind port
5050.

## Common Pitfalls

### Another Application is Running on that Port

Yahoo Messager uses 5050 and some Symantec application uses 5051.
However, there might be other applications such a IIS which can also use
those ports. Stop those applications or change the port in the
[bcp config section](../config/bcp.md).

### Firewalls and Antivirus Protection Soltions

Some firewalls might prevent MPF from binding ports. Also antivirus or
threat protection software might do that. Try if disabling those help.
If it helps see if you can add an exception for MPF.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [bcp:](../config/bcp.md)
