%global packname  quantreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.29
Release:          1%{?dist}
Summary:          Quantile Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-stats R-SparseM
# Imports:   R-methods R-graphics R-Matrix R-MatrixModels
# Suggests:  R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-Formula R-zoo
# LinkingTo:
# Enhances:


Requires:         R-stats R-SparseM 
Requires:         R-methods R-graphics R-Matrix R-MatrixModels 
Requires:         R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-Formula R-zoo 
BuildRequires:    R-devel tex(latex) R-stats R-SparseM
BuildRequires:    R-methods R-graphics R-Matrix R-MatrixModels 
BuildRequires:   R-tripack R-akima R-MASS R-survival R-rgl R-logspline R-nor1mix R-Formula R-zoo 

%description
Estimation and inference methods for models of conditional quantiles:
Linear and nonlinear parametric and non-parametric (total variation
penalized) models for conditional quantiles of a univariate response and
several methods for handling censored survival data.  Portfolio selection
methods based on expected shortfall risk are also included.

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
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/FAQ
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 5.29-1
- initial package for Fedora
