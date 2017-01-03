%global packname  logspline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.9
Release:          1%{?dist}
Summary:          Logspline Density Estimation Routines

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-stats R-graphics
# Suggests:  
# LinkingTo:
# Enhances:



Requires:         R-stats R-graphics 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-stats R-graphics 


%description
Routines for the logspline density estimation. oldlogspline() uses the
same algorithm as the logspline 1.0.x package - the Kooperberg and Stone
(1992) <DOI: 10.2307/1390786> algorithm (with an improved interface). The
recommended routine logspline() uses an algorithm from Stone et al (1997).
<DOI: 10.1214/aos/1031594728>

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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 2.1.9-1
- initial package for Fedora
