%define debug_package %{nil}
Name:       smartthing-plugin
Summary:    plugin for smartthing
Version: 1.0.0
Release:    0
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz

%description
plugin for smartthing

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib

cp -af smartthing-plugin/* %{buildroot}/

find smartthing-plugin/usr/lib/*  -exec basename {} \; | sed 's/^/\/usr\/lib\//g' >>lib.files

%files -f lib.files
%defattr(-, root, root, -)
