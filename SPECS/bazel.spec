Name:           bazel
Version:        0.3.2
Release:        1%{?dist}
Summary:        Correct, reproducible, and fast builds for everyone.
License:        Apache License 2.0
URL:            http://bazel.io/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  zlib-devel
Requires:       java-1.8.0-openjdk-devel

%define debug_package %{nil}
%define __os_install_post %{nil}

%description
Correct, reproducible, and fast builds for everyone.

%prep
%setup -q

%build

./compile.sh

%check

%install

mkdir -p %{buildroot}/%{_bindir}
cp output/bazel %{buildroot}/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/bazel

%changelog
* Fri Nov 04 2016 David Goerger <its-sa@yale.edu> - 0.3.2-1
- update to 0.3.2

* Tue Apr 12 2016 alonid <unknown@fedoraproject.org> - 0.2.1-3
- initial packaging https://copr.fedorainfracloud.org/coprs/alonid/bazel/build/174675/
