Name:		racket
Version:	6.6
Release:	1%{?dist}
Summary:	Racket is a full-spectrum programming language

Group:		Development/Languages
License:	LGPLv3
URL:		http://racket-lang.org
Source0:	http://mirror.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz

# fix rpath issue with executables
BuildRequires:	chrpath

BuildRequires:	libffi-devel
BuildRequires:	gtk3 cairo pango libpng glib2 libjpeg-turbo

# to execute DrRacket (dlopen / ffi)
Requires:	gtk3 cairo pango libpng glib2 libjpeg-turbo

# right now armv7hl build fails, exclude it until fixed
ExcludeArch: %{arm}

# prevent /usr/lib/rpm/check-buildroot, it does not exclude the *.zo files
%global __arch_install_post /usr/lib/rpm/check-rpaths

# prevent empty debuginfo package
%global debug_package %{nil}

%description
Racket is a full-spectrum programming language. It goes beyond
Lisp and Scheme with dialects that support objects, types, laziness,
and more. Racket enables programmers to link components written
in different dialects, and it empowers programmers to create new,
project-specific dialects. Racket's libraries support applications from
web servers and databases to GUIs and charts.

%package devel
Summary:	Development files for Racket
Group:		Development/Languages
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed to link against Racket.

%prep
%setup -q

rm -r src/foreign/libffi

%build
cd src
%configure \
	--enable-pthreads \
	--enable-libffi \
	--enable-shared
%make_build

%install
cd src
%make_install

## delete mred binaries and replace them with links
rm -vf ${RPM_BUILD_ROOT}%{_bindir}/mred
rm -vf ${RPM_BUILD_ROOT}%{_bindir}/mred-text
ln -vs gracket ${RPM_BUILD_ROOT}%{_bindir}/mred
ln -vs racket ${RPM_BUILD_ROOT}%{_bindir}/mred-text

## delete (possible) static library
rm -vf ${RPM_BUILD_ROOT}%{_libdir}/libracket3m.a

## fix rpath error
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/racket
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/racket/gracket

# Remove the libtool files.
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

## Fix paths in the desktop files.
sed -i "s#${RPM_BUILD_ROOT}##g" \
       ${RPM_BUILD_ROOT}/%{_datadir}/applications/*.desktop

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%files
%{_bindir}/*
%{_libdir}/lib*-*.so
%{_libdir}/racket
%{_datadir}/racket
%{_datadir}/applications/*
%{_datadir}/man/man*/*
%{_datadir}/doc/*
%{_sysconfdir}/racket/config.rktd

%files devel
%{_includedir}/*
%{_libdir}/racket/*.o
%{_libdir}/*.so

%changelog
* Fri Jul 22 2016 David Goerger <its-sa@yale.edu> - 6.6
- update to latest version

* Sat Jan 23 2016 Brandon Thomas <bthomaszx@gmail.com>
- Fixed up stylistic changes as suggested by Neal Gompa.

* Fri Jan 22 2016 Brandon Thomas <bthomaszx@gmail.com> - 6.3
- Update to current stable version.
- Updated description to match website.
- Removed build requirement "racket-packaging".
- Updated to gtk+3.
- Let Autoprovides determine provides.
- Debuginfo package is empty and preventing the package from building.
- Removed uneeded file copies.
- Remove possible extra static library.

* Sun Dec 14 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.1.6-1
- Update to current snapshot to fix match hash-table expander.

* Mon Dec 01 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.1-1
- Update to current stable version.

* Fri Sep 05 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.5-4
- Use racket-packaging to capture module dependencies.

* Tue Aug 19 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.5-1
- Updated to 6.1.0.5
- Merged the -doc package back in.

* Fri Aug 08 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.4-2
- Do not alter .zo files, prevent check-buildroot from being run instead.

* Thu Aug 07 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.4-1
- Updated to 6.1.0.4
- Split-off -doc package.

* Fri Jul 25 2014 Jan Dvorak <mordae@anilinux.org> - 6.1.0.3-4
- Updated to 6.1.0.3
- Dropped the unnecessary static library.
- Dropped mred programs to enable debug package.

* Sat Jun 22 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.5-1
- Changed to use 5.3.5 version of Racket.
- Created static package for developers who may need static libraries.
- Added RPM optimization options to CFLAGS for build.
- Added macro to use SMP build options in make.

* Thu May 16 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.4-1
- Changed to use 5.3.4 version of Racket.

* Tue May 14 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-3
- Moved documentation to /usr/doc directory.

* Mon May 13 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-2
- Remove bundled libffi from racket before building program.

* Thu May  9 2013 Daniel E. Wilson <danw@bureau-13.org> - 5.3.3-1
- Initial Revision.
