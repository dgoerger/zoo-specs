%global packname  svglite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          An 'SVG' Graphics Device

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-Rcpp R-gdtools
# Suggests:  R-htmltools R-testthat R-xml2 R-covr R-fontquiver R-knitr R-rmarkdown
# LinkingTo:
# Enhances:



Requires:         R-Rcpp R-gdtools 
Requires:         R-htmltools R-testthat R-xml2 R-covr R-knitr R-rmarkdown 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Rcpp R-Rcpp-devel R-gdtools
BuildRequires:   R-htmltools R-testthat R-xml2 R-covr R-knitr R-rmarkdown 

%description
A graphics device for R that produces 'Scalable Vector Graphics'.
'svglite' is a fork of the older 'RSvgDevice' package.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.2.0-1
- initial package for Fedora
