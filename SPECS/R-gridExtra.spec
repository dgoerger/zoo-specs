%global packname  gridExtra
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Miscellaneous Functions for "Grid" Graphics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-gtable R-grid R-grDevices R-graphics R-utils
# Suggests:  R-ggplot2 R-lattice R-knitr R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-gtable R-grid R-grDevices R-graphics R-utils 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-gtable R-grid R-grDevices R-graphics R-utils 

%description
Provides a number of user-level functions to work with "grid" graphics,
notably to arrange multiple grid-based plots on a page, and draw tables.

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
%{rlibdir}/%{packname}/tests


%changelog
* Tue Dec 13 2016 deg38 <> 2.2.1-1
- initial package for Fedora
