%define debug_package %{nil}
%global packname  foreach
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          Provides Foreach Looping Construct for R

Group:            Applications/Engineering 
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-codetools R-utils R-iterators
# Suggests:  R-randomForest
# LinkingTo:
# Enhances:



Requires:         R-codetools R-utils R-iterators 
Requires:         R-randomForest 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-codetools R-utils R-iterators 
BuildRequires:   R-randomForest 

%description
Support for the foreach looping construct.  Foreach is an idiom that
allows for iterating over elements in a collection, without the use of an
explicit loop counter.  This package in particular is intended to be used
for its return value, rather than for its side effects.  In that sense, it
is similar to the standard lapply function, but doesn't require the
evaluation of a function.  Using foreach without side effects also
facilitates executing the loop in parallel.

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
* Tue Dec 13 2016 deg38 <> 1.4.3-1
- initial package for Fedora
