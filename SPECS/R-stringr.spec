%global packname stringr
%global packrel 1
%global debug_package %{nil}

Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
License:          GPLv2+
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Wrappers around R-stringi
BuildRequires:    R-devel
BuildRequires:    R-stringi, R-magrittr
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-stringi, R-magrittr

%description
R interface to stringr. A consistent, simple and easy to use set of wrappers
around the fantastic 'stringi' package. All function and argument names (and
positions) are consistent, all functions deal with "NA"'s and zero length
vectors in the same way, and the output from one function is easy to feed
into the input of another.

%prep
%setup -q -c -n %{packname}

# empty file warning
rm -rf debugfiles.list

%build

%install
rm -rf $RPM_BUILD_ROOT
# empty file warning
rm -rf debugfiles.list

mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL --install-tests --build -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css


%check
export _R_CHECK_FORCE_SUGGESTS_=false
#%{_bindir}/R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/tests*

%changelog
* Tue Jul 26 2016 David Goerger <its-sa@yale.edu> 1.0.0-1
- initial package creation
