%global packname  scales
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Scale Functions for Visualization

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-RColorBrewer R-dichromat R-plyr R-munsell R-labeling R-methods R-Rcpp
# Suggests:  R-testthat R-covr R-hms
# LinkingTo:
# Enhances:



Requires:         R-RColorBrewer R-dichromat R-plyr R-munsell R-labeling R-methods R-Rcpp 
Requires:         R-testthat R-covr R-hms 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-RColorBrewer R-dichromat R-plyr R-munsell R-labeling R-methods R-Rcpp R-Rcpp-devel
BuildRequires:   R-testthat R-covr R-hms 

%description
Graphical scales map data to aesthetics, and provide methods for
automatically determining breaks and labels for axes and legends.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 0.4.1-1
- initial package for Fedora
