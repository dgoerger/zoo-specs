%global packname  htmlwidgets
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          HTML Widgets for R

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-htmltools R-jsonlite R-yaml
# Suggests:  R-knitr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-htmltools R-jsonlite R-yaml 
Requires:         R-knitr 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-htmltools R-jsonlite R-yaml 
BuildRequires:   R-knitr 

%description
A framework for creating HTML widgets that render in various contexts
including the R console, 'R Markdown' documents, and 'Shiny' web

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
%{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/www


%changelog
* Tue Dec 13 2016 deg38 <> 0.8-1
- initial package for Fedora
