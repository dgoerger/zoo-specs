%global packname  LaF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Fast access to large ASCII files

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-Rcpp
# Suggests:  R-testthat R-yaml
# LinkingTo:
# Enhances:


Requires:         R-methods 
Requires:         R-Rcpp
Requires:         R-testthat R-yaml 
BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-Rcpp R-Rcpp-devel
BuildRequires:   R-testthat R-yaml R-R6

%description
Methods for fast access to large ASCII files.  Currently the following
file formats are supported: comma separated format (csv) and fixed width
format. It is assumed that the files are too large to fit into memory,
although the package can also be used to efficiently access files that do
fit into memory. Methods are provided to access and process files
blockwise. Furthermore, an opened file can be accessed as one would an
ordinary data.frame. The LaF vignette gives an overview of the
functionality provided.

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
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 0.6.2-1
- initial package for Fedora
