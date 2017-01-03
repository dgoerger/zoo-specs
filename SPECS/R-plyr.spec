%global packname  plyr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.4
Release:          1%{?dist}
Summary:          Tools for Splitting, Applying and Combining Data

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-Rcpp
# Suggests:  R-abind R-testthat R-tcltk R-foreach R-doParallel R-itertools R-iterators R-covr
# LinkingTo:
# Enhances:



Requires:         R-Rcpp 
Requires:         R-abind R-testthat R-tcltk R-foreach R-doParallel R-itertools R-iterators R-covr 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Rcpp R-Rcpp-devel
BuildRequires:   R-abind R-testthat R-tcltk R-foreach R-doParallel R-itertools R-iterators R-covr

%description
A set of tools that solves a common set of problems: you need to break a
big problem down into manageable pieces, operate on each piece and then
put all the pieces back together.  For example, you might want to fit a
model to each spatial location or time point in your study, summarise data
by panels or collapse high-dimensional arrays to simpler summary
statistics. The development of 'plyr' has been generously supported by
'Becton Dickinson'.

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
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.8.4-1
- initial package for Fedora
