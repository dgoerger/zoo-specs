Name:		clang
Version:	3.8.0
Release:	101%{?dist}
Summary:	A C language family front-end for LLVM

License:	NCSA
URL:		http://llvm.org
Source0:	http://llvm.org/releases/%{version}/cfe-%{version}.src.tar.xz
Source1:	http://llvm.org/releases/%{version}/clang-tools-extra-%{version}.src.tar.xz

Source100:	clang-config.h

Patch0:		0001-GCC-PR23529-Sema-part-of-attrbute-abi_tag-support.patch
Patch1:		0002-GCC-PR23529-Mangler-part-of-attrbute-abi_tag-support.patch

BuildRequires:	cmake
BuildRequires:	llvm-devel = %{version}
BuildRequires:	libxml2-devel
BuildRequires:  llvm-static = %{version}
BuildRequires:  tar

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:	libstdc++-devel
Requires:	gcc-c++

%description
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.

%package libs
Summary: Runtime library for clang
Requires: compiler-rt%{?_isa} >= %{version}

%description libs
Runtime library for clang.

%package devel
Summary: Development header files for clang.
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development header files for clang.

%package analyzer
Summary:	A source code analysis framework
License:	NCSA and MIT
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
# not picked up automatically since files are currently not installed in
# standard Python hierarchies yet
Requires:	python

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package tools-extra
Summary: Extra tools for clang
Requires:       %{name} = %{version}-%{release}
Provides:       clang-apply-replacements
Provides:       clang-query
Provides:       clang-rename
Provides:       clang-tidy

%description tools-extra
Extra tools for clang.

%prep
%setup -q -n cfe-%{version}.src clang-tools-extra-%{version}.src
%patch0 -p1
%patch1 -p1
%build
tar -xf %{SOURCE1}
mv clang-tools-extra-%{version}.src tools/extra
mkdir -p _build
cd _build
%cmake .. \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DLLVM_CONFIG:FILEPATH=/usr/bin/llvm-config-%{__isa_bits} \
	\
	-DCLANG_ENABLE_ARCMT:BOOL=ON \
	-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
	-DCLANG_INCLUDE_DOCS:BOOL=ON \
	-DCLANG_INCLUDE_TESTS:BOOL=ON \
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	\
	-DCLANG_BUILD_EXAMPLES:BOOL=OFF \
	-DLIB_SUFFIX=

make %{?_smp_mflags}

%install
cd _build
make install DESTDIR=%{buildroot}

# multilib fix
mv -v %{buildroot}%{_includedir}/clang/Config/config{,-%{__isa_bits}}.h
install -m 0644 %{SOURCE100} %{buildroot}%{_includedir}/clang/Config/config.h

# remove git integration
rm -vf %{buildroot}%{_bindir}/git-clang-format
# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*
rm -vf %{buildroot}%{_datadir}/clang/clang-format.el
rm -vf %{buildroot}%{_datadir}/clang/clang-format.py*
# remove diff reformatter
rm -vf %{buildroot}%{_datadir}/clang/clang-format-diff.py*

%check
# requires lit.py from LLVM utilities
#cd _build
#make check-all

%files
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}++
%{_bindir}/%{name}-3.8
%{_bindir}/%{name}-check
%{_bindir}/%{name}-cl
%{_bindir}/%{name}-format
%{_bindir}/c-index-test
%{_bindir}/modularize

%files libs
%{_libdir}/*.so.*
%{_libdir}/*.so

%files devel
%{_includedir}/%{name}/
%{_includedir}/clang-c/
%{_datadir}/%{name}/
%{_datadir}/%{name}/cmake/

%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_bindir}/scan-build
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*

%files tools-extra
%{_bindir}/%{name}-apply-replacements
%{_bindir}/%{name}-query
%{_bindir}/%{name}-rename
%{_bindir}/%{name}-tidy

%changelog
* Wed Nov 16 2016 David Goerger <david.goerger@yale.edu> - 3.8.0-101
- add clang-tools-extra

* Mon Nov 14 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.8.0-3
- Add Requires: compiler-rt to clang-libs.
- Without this, compiling with certain CFLAGS breaks.

* Fri Jul 01 2016 Stephan Bergmann <sbergman@redhat.com> - 3.8.0-2
- Resolves: rhbz#1282645 add GCC abi_tag support

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- clang 3.8.0 final release

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.4
- clang 3.8.0rc3

* Wed Feb 24 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.3
- package all libs into clang-libs.

* Wed Feb 24 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- enable dynamic linking of clang against llvm

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.1
- clang 3.8.0rc2

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- rebuild against latest llvm packages
- add BuildRequires llvm-static

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Dave Airlie <airlied@redhat.com> 3.7.1-2
- just accept clang includes moving to /usr/lib64, upstream don't let much else happen

* Thu Jan 28 2016 Dave Airlie <airlied@redhat.com> 3.7.1-1
- initial build in Fedora.

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
