#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-143-1-0."""

import core
from tr098_v1_1 import InternetGatewayDevice_v1_2
from tr106_v1_1 import Device_v1_1


class Device_v1_2(Device_v1_1):
  """Represents Device_v1_2."""

  def __init__(self, **defaults):
    Device_v1_1.__init__(self, defaults=defaults)
    self.Export(objects=['Capabilities',
                         'DownloadDiagnostics',
                         'UDPEchoConfig',
                         'UploadDiagnostics'])

  class Capabilities(core.Exporter):
    """Represents Device_v1_2.Capabilities."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(objects=['PerformanceDiagnostic'])

    class PerformanceDiagnostic(core.Exporter):
      """Represents Device_v1_2.Capabilities.PerformanceDiagnostic."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['DownloadTransports',
                            'UploadTransports'])

  class DownloadDiagnostics(core.Exporter):
    """Represents Device_v1_2.DownloadDiagnostics."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BOMTime',
                          'DSCP',
                          'DiagnosticsState',
                          'DownloadURL',
                          'EOMTime',
                          'EthernetPriority',
                          'Interface',
                          'ROMTime',
                          'TCPOpenRequestTime',
                          'TCPOpenResponseTime',
                          'TestBytesReceived',
                          'TotalBytesReceived'])

  class UDPEchoConfig(core.Exporter):
    """Represents Device_v1_2.UDPEchoConfig."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BytesReceived',
                          'BytesResponded',
                          'EchoPlusEnabled',
                          'EchoPlusSupported',
                          'Enable',
                          'Interface',
                          'PacketsReceived',
                          'PacketsResponded',
                          'SourceIPAddress',
                          'TimeFirstPacketReceived',
                          'TimeLastPacketReceived',
                          'UDPPort'])

  class UploadDiagnostics(core.Exporter):
    """Represents Device_v1_2.UploadDiagnostics."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BOMTime',
                          'DSCP',
                          'DiagnosticsState',
                          'EOMTime',
                          'EthernetPriority',
                          'Interface',
                          'ROMTime',
                          'TCPOpenRequestTime',
                          'TCPOpenResponseTime',
                          'TestFileLength',
                          'TotalBytesSent',
                          'UploadURL'])


class InternetGatewayDevice_v1_3(InternetGatewayDevice_v1_2):
  """Represents InternetGatewayDevice_v1_3."""

  def __init__(self, **defaults):
    InternetGatewayDevice_v1_2.__init__(self, defaults=defaults)
    self.Export(objects=['Capabilities',
                         'DownloadDiagnostics',
                         'UDPEchoConfig',
                         'UploadDiagnostics'])

  class Capabilities(core.Exporter):
    """Represents InternetGatewayDevice_v1_3.Capabilities."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(objects=['PerformanceDiagnostic'])

    class PerformanceDiagnostic(core.Exporter):
      """Represents InternetGatewayDevice_v1_3.Capabilities.PerformanceDiagnostic."""

      def __init__(self, **defaults):
        core.Exporter.__init__(self, defaults=defaults)
        self.Export(params=['DownloadTransports',
                            'UploadTransports'])

  class DownloadDiagnostics(core.Exporter):
    """Represents InternetGatewayDevice_v1_3.DownloadDiagnostics."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BOMTime',
                          'DSCP',
                          'DiagnosticsState',
                          'DownloadURL',
                          'EOMTime',
                          'EthernetPriority',
                          'Interface',
                          'ROMTime',
                          'TCPOpenRequestTime',
                          'TCPOpenResponseTime',
                          'TestBytesReceived',
                          'TotalBytesReceived'])

  class UDPEchoConfig(core.Exporter):
    """Represents InternetGatewayDevice_v1_3.UDPEchoConfig."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BytesReceived',
                          'BytesResponded',
                          'EchoPlusEnabled',
                          'EchoPlusSupported',
                          'Enable',
                          'Interface',
                          'PacketsReceived',
                          'PacketsResponded',
                          'SourceIPAddress',
                          'TimeFirstPacketReceived',
                          'TimeLastPacketReceived',
                          'UDPPort'])

  class UploadDiagnostics(core.Exporter):
    """Represents InternetGatewayDevice_v1_3.UploadDiagnostics."""

    def __init__(self, **defaults):
      core.Exporter.__init__(self, defaults=defaults)
      self.Export(params=['BOMTime',
                          'DSCP',
                          'DiagnosticsState',
                          'EOMTime',
                          'EthernetPriority',
                          'Interface',
                          'ROMTime',
                          'TCPOpenRequestTime',
                          'TCPOpenResponseTime',
                          'TestFileLength',
                          'TotalBytesSent',
                          'UploadURL'])


if __name__ == '__main__':
  print core.DumpSchema(Device_v1_2)
  print core.DumpSchema(InternetGatewayDevice_v1_3)
