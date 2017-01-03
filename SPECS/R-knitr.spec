%define debug_package %{nil}
%global packname  knitr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.15.1
Release:          1%{?dist}
Summary:          A General-Purpose Package for Dynamic Report Generation in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-evaluate R-digest R-highr R-markdown R-stringr R-yaml R-methods R-tools
# Suggests:  R-formatR R-testit R-rgl R-codetools R-rmarkdown R-htmlwidgets R-webshot R-tikzDevice R-png R-jpeg R-XML R-RCurl R-DBI R-tibble
# LinkingTo:
# Enhances:



Requires:         R-evaluate R-digest R-highr R-markdown R-stringr R-yaml R-methods R-tools 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-evaluate R-digest R-highr R-markdown R-stringr R-yaml R-methods R-tools 

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/opencpu
%{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/themes


%changelog
* Tue Dec 13 2016 deg38 <> 1.15.1-1
- initial package for Fedora
