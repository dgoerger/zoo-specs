%global packname  hash
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.6
Release:          1%{?dist}
Summary:          Full feature implementation of hash/associated arrays/dictionaries

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods R-utils
# Imports:   
# Suggests:  R-testthat
# LinkingTo:
# Enhances:


Requires:         R-methods R-utils 

Requires:         R-testthat 
BuildRequires:    R-devel tex(latex) R-methods R-utils

BuildRequires:   R-testthat 

%description
This package implements a data structure similar to hashes in Perl and
dictionaries in Python but with a purposefully R flavor.  For objects of
appreciable size, access using hashes outperforms native named lists and

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


%changelog
* Fri Jun 30 2017 deg38 <> 2.2.6-1
- initial package for Fedora