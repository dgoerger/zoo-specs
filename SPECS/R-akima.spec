%global packname  akima
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.12
Release:          1%{?dist}
Summary:          Interpolation of Irregularly and Regularly Spaced Data

Group:            Applications/Engineering 
License:          ACM | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-sp
# Suggests:  
# LinkingTo:
# Enhances:



Requires:         R-sp 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-sp 


%description
Several cubic spline interpolation methods of H. Akima for irregular and
regular gridded data are available through this package, both for the
bivariate case (irregular data: ACM 526 and ACM 761, regular data: ACM
433) and univariate case (ACM 697). Linear interpolation of irregular
gridded data is also covered by reusing D. J. Renkas triangulation code
which is part of Akimas Fortran code.

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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 0.5.12-1
- initial package for Fedora
