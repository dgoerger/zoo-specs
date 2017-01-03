%global packname  SparseM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.74
Release:          1%{?dist}
Summary:          Sparse Linear Algebra

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-graphics R-stats R-utils
# Suggests:  
# LinkingTo:
# Enhances:


Requires:         R-methods 
Requires:         R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-graphics R-stats R-utils 


%description
Some basic linear algebra functionality for sparse matrices is provided: 
including Cholesky decomposition and backsolving as well as standard R
subsetting and Kronecker products.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 1.74-1
- initial package for Fedora
