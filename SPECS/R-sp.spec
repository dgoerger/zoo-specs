%global packname  sp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Classes and Methods for Spatial Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils R-stats R-graphics R-grDevices R-lattice R-grid
# Suggests:  R-RColorBrewer R-rgdal R-rgeos R-gstat R-maptools R-deldir
# LinkingTo:
# Enhances:


Requires:         R-methods 
Requires:         R-utils R-stats R-graphics R-grDevices R-lattice R-grid 
BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-utils R-stats R-graphics R-grDevices R-lattice R-grid 

%description
Classes and methods for spatial data; the classes document where the
spatial location information resides, for 2D or 3D data. Utility functions
are provided, e.g. for plotting data as maps, spatial selection, as well
as methods for retrieving coordinates, for subsetting, print, summary,

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.2.3-1
- initial package for Fedora
