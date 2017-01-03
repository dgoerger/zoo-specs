%global packname  raster
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.5.8
Release:          1%{?dist}
Summary:          Geographic Data Analysis and Modeling

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.5-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods R-sp
# Imports:   R-Rcpp
# Suggests:  R-rgdal R-rgeos R-ncdf4 R-igraph R-tcltk R-parallel R-rasterVis
# LinkingTo:
# Enhances:


Requires:         R-methods R-sp 
Requires:         R-Rcpp 
BuildRequires:    R-devel tex(latex) R-methods R-sp
BuildRequires:    R-Rcpp R-Rcpp-devel

%description
Reading, writing, manipulating, analyzing and modeling of gridded spatial
data. The package implements basic and high-level functions. Processing of
very large files is supported.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 2.5.8-1
- initial package for Fedora
