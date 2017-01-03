%global packname  maps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.1
Release:          1%{?dist}
Summary:          Draw Geographical Maps

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-graphics R-utils
# Suggests:  R-mapproj R-mapdata R-sp R-maptools
# LinkingTo:
# Enhances:



Requires:         R-graphics R-utils 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-utils 

%description
Display of maps.  Projection code and larger maps are in separate packages
('mapproj' and 'mapdata').

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/README.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/mapdata


%changelog
* Tue Dec 13 2016 deg38 <> 3.1.1-1
- initial package for Fedora
