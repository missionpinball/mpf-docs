File Interfaces
===============

MPF's file interface module contains the base code on which MPF file interface implementations are built. MPF is
architected in such a way that the actual file interface is separate from the MPF interface. This means that separate
file interfaces could be created for YAML. XML, JSON, etc.