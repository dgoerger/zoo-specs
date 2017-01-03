%define debug_package %{nil}
%global packname  shiny
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.14.2
Release:          1%{?dist}
Summary:          Web Application Framework for R

Group:            Applications/Engineering 
License:          GPL-3 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils R-httpuv R-mime R-jsonlite R-xtable R-digest R-htmltools R-R6 R-sourcetools
# Suggests:  R-datasets R-Cairo R-testthat R-knitr R-markdown R-rmarkdown R-ggplot2
# LinkingTo:
# Enhances:


Requires:         R-methods 
Requires:         R-utils R-httpuv R-mime R-jsonlite R-xtable R-digest R-htmltools R-R6 R-sourcetools 
BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-utils R-httpuv R-mime R-jsonlite R-xtable R-digest R-htmltools R-R6 R-sourcetools 

%description
Makes it incredibly easy to build interactive web applications with R.
Automatic "reactive" binding between inputs and outputs and extensive
pre-built widgets make it possible to build beautiful, responsive, and
powerful applications with minimal effort.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/staticdocs
%{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/www-dir


%changelog
* Tue Dec 13 2016 deg38 <> 0.14.2-1
- initial package for Fedora
