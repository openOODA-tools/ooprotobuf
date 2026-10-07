Name:           ooprotobuf
Version:        0.1.0
Release:        1%{?dist}
Summary:        Decodes Protocol Buffer wire format without needing compiled proto stubs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooprotobuf
Source0:        ooprotobuf-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooprotobuf is a sovereign, capability-bounded PROTOBUF DECODER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooprotobuf
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooprotobuf-uninstall

%files
/usr/bin/ooprotobuf
/usr/bin/ooprotobuf-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
