%global packname  markdown
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.7
Release:          1%{?dist}
Summary:          'Markdown' Rendering for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-mime
# Suggests:  R-knitr R-RCurl
# LinkingTo:
# Enhances:



Requires:         R-mime 
Requires:         R-RCurl 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mime 
BuildRequires:    R-RCurl 

%description
Provides R bindings to the 'Sundown' 'Markdown' rendering library
(https://github.com/vmg/sundown). 'Markdown' is a plain-text formatting
syntax that can be converted to 'XHTML' or other formats. See
http://en.wikipedia.org/wiki/Markdown for more information about

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
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/resources



%changelog
* Tue Dec 13 2016 deg38 <> 0.7.7-1
- initial package for Fedora
