%define debug_package %{nil}
%global packname  rmarkdown
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Dynamic Documents for R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-tools R-utils R-grDevices R-knitr R-yaml R-htmltools R-caTools R-evaluate R-base64enc R-jsonlite R-rprojroot R-methods
# Suggests:  R-shiny R-tufte R-testthat R-digest R-tibble
# LinkingTo:
# Enhances:



Requires:         R-tools R-utils R-grDevices R-knitr R-yaml R-htmltools R-caTools R-evaluate R-base64enc R-jsonlite R-rprojroot R-methods 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-tools R-utils R-grDevices R-knitr R-yaml R-htmltools R-caTools R-evaluate R-base64enc R-jsonlite R-rprojroot R-methods 

%description
Convert R Markdown documents into a variety of formats.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/rmd


%changelog
* Tue Dec 13 2016 deg38 <> 1.2-1
- initial package for Fedora
