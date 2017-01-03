%global packname  htmlTable
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Advanced Tables for Markdown/HTML

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-stringr R-knitr R-magrittr R-methods
# Suggests:  R-testthat R-XML R-xtable R-ztable R-Hmisc R-reshape R-rmarkdown R-pander
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-stringr R-knitr R-magrittr R-methods 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-stringr R-knitr R-magrittr R-methods 

%description
Tables with state-of-the-art layout elements such as row spanners, column
spanners, table spanners, zebra striping, and more. While allowing
advanced layout, the underlying css-structure is simple in order to
maximize compatibility with word processors such as 'MS Word' or
'LibreOffice'. The package also contains a few text formatting functions
that help outputting text compatible with HTML/'LaTeX'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/html_components
%{rlibdir}/%{packname}/javascript


%changelog
* Tue Dec 13 2016 deg38 <> 1.7-1
- initial package for Fedora
