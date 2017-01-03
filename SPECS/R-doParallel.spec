%define debug_package %{nil}
%global packname  doParallel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.10
Release:          1%{?dist}
Summary:          Foreach Parallel Adaptor for the 'parallel' Package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-foreach R-iterators R-parallel R-utils
# Imports:   
# Suggests:  R-caret R-mlbench R-rpart
# LinkingTo:
# Enhances:


Requires:         R-foreach R-iterators R-parallel R-utils 

BuildRequires:    R-devel tex(latex) R-foreach R-iterators R-parallel R-utils

%description
Provides a parallel backend for the %dopar% function using the parallel

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
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/unitTests


%changelog
* Tue Dec 13 2016 deg38 <> 1.0.10-1
- initial package for Fedora
