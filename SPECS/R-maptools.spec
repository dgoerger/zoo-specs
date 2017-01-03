%global packname  maptools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.40
Release:          1%{?dist}
Summary:          Tools for Reading and Handling Spatial Objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-40.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-sp
# Imports:   R-foreign R-methods R-grid R-lattice R-stats R-utils R-grDevices
# Suggests:  R-rgeos R-spatstat R-PBSmapping R-maps R-RColorBrewer R-raster R-polyclip
# LinkingTo:
# Enhances:


Requires:         R-sp 
Requires:         R-foreign R-methods R-grid R-lattice R-stats R-utils R-grDevices 
BuildRequires:    R-devel tex(latex) R-sp
BuildRequires:    R-foreign R-methods R-grid R-lattice R-stats R-utils R-grDevices 

%description
Set of tools for manipulating and reading geographic data, in particular
'ESRI Shapefiles'; C code used from 'shapelib'. It includes binary access
to 'GSHHG' shoreline files. The package also provides interface wrappers
for exchanging spatial objects with packages such as 'PBSmapping',
'spatstat', 'maps', 'RArcInfo', 'Stata tmap', 'WinBUGS', 'Mondrian', and

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
%{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/changes
%{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/grids
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/share


%changelog
* Tue Dec 13 2016 deg38 <> 0.8.40-1
- initial package for Fedora
