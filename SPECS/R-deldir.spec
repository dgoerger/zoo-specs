%global packname  deldir
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.12
Release:          1%{?dist}
Summary:          Delaunay Triangulation and Dirichlet (Voronoi) Tessellation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-graphics R-grDevices
# Suggests:  R-polyclip
# LinkingTo:
# Enhances:



Requires:         R-graphics R-grDevices 
Requires:         R-polyclip 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices 
BuildRequires:   R-polyclip 

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.
Plots triangulations and tessellations in various ways.  Clips
tessellations to sub-windows. Calculates perimeters of tessellations.

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
%{rlibdir}/%{packname}/READ_ME
%{rlibdir}/%{packname}/code.discarded
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/err.list
%{rlibdir}/%{packname}/ex.out
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/ratfor


%changelog
* Tue Dec 13 2016 deg38 <> 0.1.12-1
- initial package for Fedora
