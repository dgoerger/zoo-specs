%global debug_package %{nil}
%global packname testthat
%global packver 1.0.2

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}.tar.gz
License:          MIT
URL:              http://cran.r-project.org/web/packages/testthat/index.html
Group:            Applications/Engineering
Summary:          Unit Testing for R
BuildRequires:    R-devel >= 3.1.0, tetex-latex, R-digest-devel, R-crayon, R-praise, R-R6, R-magrittr
Requires:         R-core >= 3.1.0, R-digest, R-crayon, R-praise, R-magrittr

%description
A unit testing system designed to be fun, flexible, and easy to set up.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
# Not the actual license text. Not too useful.
%doc %{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/include/
%{_libdir}/R/library/%{packname}/resources/


%changelog
* Tue Sep 06 2016 David Goerger <its-sa@yale.edu> - 1.0.2-1
- update to 1.0.2, needed for R-swirl

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.11.0-2
- fix define to be global

* Wed Nov 4 2015 Tom Callaway <spot@fedoraproject.org> - 0.11.0-1
- Initial package
