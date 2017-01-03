%global packname  cluster
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          "Finding Groups in Data": Cluster Analysis Extended Rousseeuw et al.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-graphics R-grDevices R-stats R-utils
# Suggests:  R-MASS
# LinkingTo:
# Enhances:



Requires:         R-graphics R-grDevices R-stats R-utils 
Requires:         R-MASS 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-stats R-utils 
BuildRequires:   R-MASS 

%description
Methods for Cluster analysis.  Much extended the original from Peter
Rousseeuw, Anja Struyf and Mia Hubert, based on Kaufman and Rousseeuw
(1990) "Finding Groups in Data".

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po


%changelog
* Tue Dec 13 2016 deg38 <> 2.0.5-1
- initial package for Fedora
