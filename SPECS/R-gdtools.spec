%global packname  gdtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Utilities for Graphical Rendering

Group:            Applications/Engineering 
License:          GPL-3 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-Rcpp R-withr
# Suggests:  R-htmltools R-testthat R-fontquiver
# LinkingTo:
# Enhances:



Requires:         R-Rcpp R-withr 
Requires:         R-htmltools R-testthat cairo
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Rcpp R-Rcpp-devel R-withr 
BuildRequires:    R-htmltools R-testthat cairo-devel

%description
Useful tools for writing vector graphics devices.

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
%{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/fontconfig
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 0.1.3-1
- initial package for Fedora
