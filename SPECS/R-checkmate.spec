%global packname  checkmate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.2
Release:          1%{?dist}
Summary:          Fast and Versatile Argument Checks

Group:            Applications/Engineering 
License:          BSD_3_clause + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-backports R-utils
# Suggests:  R-data.table R-devtools R-ggplot2 R-knitr R-rmarkdown R-magrittr R-microbenchmark R-testthat R-tibble
# LinkingTo:
# Enhances:



Requires:         R-backports R-utils 
Requires:         R-data.table R-devtools R-ggplot2 R-knitr R-rmarkdown R-magrittr R-microbenchmark R-testthat R-tibble 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-backports R-utils 
BuildRequires:   R-data.table R-devtools R-ggplot2 R-knitr R-rmarkdown R-magrittr R-microbenchmark R-testthat R-tibble 

%description
Tests and assertions to perform frequent argument checks. A substantial
part of the package was written in C to minimize any worries about
execution time overhead.

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
* Tue Dec 13 2016 deg38 <> 1.8.2-1
- initial package for Fedora