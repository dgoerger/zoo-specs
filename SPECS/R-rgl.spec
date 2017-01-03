%global packname  rgl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.96.0
Release:          1%{?dist}
Summary:          3D Visualization Using OpenGL

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-graphics R-grDevices R-stats R-utils R-htmlwidgets R-htmltools R-knitr R-jsonlite R-shiny R-magrittr
# Suggests:  R-MASS R-rmarkdown R-deldir R-orientlib R-lattice R-misc3d R-rstudioapi
# LinkingTo:
# Enhances:



Requires:         R-graphics R-grDevices R-stats R-utils R-htmlwidgets R-htmltools R-knitr R-jsonlite R-shiny R-magrittr 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-stats R-utils R-htmlwidgets R-htmltools R-knitr R-jsonlite R-shiny R-magrittr mesa-libGLU-devel

%description
Provides medium to high level functions for 3D interactive graphics,
including functions modelled on base graphics (plot3d(), etc.) as well as
functions for constructing representations of geometric objects (cube3d(),
etc.).  Output may be on screen using OpenGL, or to various standard 3D
file formats including WebGL, PLY, OBJ, STL as well as 2D image formats,
including PNG, Postscript, SVG, PGF.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WebGL
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/demodata
%{rlibdir}/%{packname}/fonts
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/initNotes.txt
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/shinyDemo
%{rlibdir}/%{packname}/shinySimple
%{rlibdir}/%{packname}/textures


%changelog
* Tue Dec 13 2016 deg38 <> 0.96.0-1
- initial package for Fedora
