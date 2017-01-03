%global packname  tidyverse
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Easily Install and Load 'Tidyverse' Packages

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-broom R-DBI R-dplyr R-forcats R-ggplot2 R-haven R-httr R-hms R-jsonlite R-lubridate R-magrittr R-modelr R-purrr R-readr R-readxl R-stringr R-tibble R-rvest R-tidyr R-xml2
# Suggests:  R-knitr R-rmarkdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-broom R-DBI R-dplyr R-forcats R-ggplot2 R-haven R-httr R-hms R-jsonlite R-lubridate R-magrittr R-modelr R-purrr R-readr R-readxl R-stringr R-tibble R-rvest R-tidyr R-xml2 
Requires:         R-knitr R-rmarkdown 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-broom R-DBI R-dplyr R-forcats R-ggplot2 R-haven R-httr R-hms R-jsonlite R-lubridate R-magrittr R-modelr R-purrr R-readr R-readxl R-stringr R-tibble R-rvest R-tidyr R-xml2 
BuildRequires:   R-knitr R-rmarkdown 

%description
The 'tidyverse' is a set of packages that work in harmony because they
share common data representations and 'API' design. This package is
designed to make it easy to install and load multiple 'tidyverse' packages
in a single step. Learn more about the 'tidyverse' at

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
* Tue Dec 13 2016 deg38 <> 1.0.0-1
- initial package for Fedora