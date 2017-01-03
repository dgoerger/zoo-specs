%global packname  rasterVis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.41
Release:          1%{?dist}
Summary:          Visualization Methods for Raster Data

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods R-raster R-lattice R-latticeExtra
# Imports:   R-stats R-utils R-parallel R-grid R-grDevices R-RColorBrewer R-hexbin R-sp R-zoo R-viridisLite
# Suggests:  R-rgl R-ggplot2 R-colorspace R-dichromat
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-raster R-lattice R-latticeExtra 
Requires:         R-stats R-utils R-parallel R-grid R-grDevices R-RColorBrewer R-hexbin R-sp R-zoo R-viridisLite 
Requires:         R-rgl R-ggplot2 R-colorspace R-dichromat 
BuildRequires:    R-devel tex(latex) R-methods R-raster R-lattice R-latticeExtra
BuildRequires:    R-stats R-utils R-parallel R-grid R-grDevices R-RColorBrewer R-hexbin R-sp R-zoo R-viridisLite 
BuildRequires:   R-rgl R-ggplot2 R-colorspace R-dichromat 

%description
Methods for enhanced visualization and interaction with raster data. It
implements visualization methods for quantitative data and categorical
data, both for univariate and multivariate rasters. It also provides
methods to display spatiotemporal rasters, and vector fields. See the
website for examples.

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
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Tue Dec 13 2016 deg38 <> 0.41-1
- initial package for Fedora
