%global packname stringi
%global packrel 1

Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
License:          Custom
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Portable string processing for R
BuildRequires:    R-devel
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-core

%description
Allows for fast, correct, consistent, portable, as well as convenient character string/text processing in every locale and any native encoding. Owing to the use of the ICU library, the package provides R users with platform-independent functions known to Java, Perl, Python, PHP, and Ruby programmers. Among available features there are: pattern searching (e.g., with ICU Java-like regular expressions or the Unicode Collation Algorithm), random string generation, case mapping, string transliteration, concatenation, Unicode normalization, date-time formatting and parsing, etc.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/AUTHORS
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/include/stringi.cpp
%{_libdir}/R/library/%{packname}/include/stringi.h
%{_libdir}/R/library/%{packname}/libs/stringi.so


%changelog
* Tue Jul 26 2016 David Goerger <its-sa@yale.edu> 1.1.1-1
- initial package creation
