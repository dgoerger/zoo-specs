%global packname  ff
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.13
Release:          1%{?dist}
Summary:          memory-efficient storage of large data on disk and fast access functions

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-bit R-utils
# Imports:   
# Suggests:  R-biglm
# LinkingTo:
# Enhances:


Requires:         R-bit R-utils 

Requires:         R-biglm 
BuildRequires:    R-devel tex(latex) R-bit R-utils

BuildRequires:   R-biglm 

%description
The ff package provides data structures that are stored on disk but behave
(almost) as if they were in RAM by transparently mapping only a section
(pagesize) in main memory - the effective virtual memory consumption per
ff object. ff supports R's standard atomic data types 'double', 'logical',
'raw' and 'integer' and non-standard atomic types boolean (1 bit), quad (2
bit unsigned), nibble (4 bit unsigned), byte (1 byte signed with NAs),
ubyte (1 byte unsigned), short (2 byte signed with NAs), ushort (2 byte
unsigned), single (4 byte float with NAs). For example 'quad' allows
efficient storage of genomic data as an 'A','T','G','C' factor. The
unsigned types support 'circular' arithmetic. There is also support for
close-to-atomic types 'factor', 'ordered', 'POSIXct', 'Date' and custom
close-to-atomic types. ff not only has native C-support for vectors,
matrices and arrays with flexible dimorder (major column-order, major
row-order and generalizations for arrays). There is also a ffdf class not
unlike data.frames and import/export filters for csv files. ff objects
store raw data in binary flat files in native encoding, and complement
this with metadata stored in R as physical and virtual attributes. ff
objects have well-defined hybrid copying semantics, which gives rise to
certain performance improvements through virtualization. ff objects can be
stored and reopened across R sessions. ff files can be shared by multiple
ff R objects (using different data en/de-coding schemes) in the same
process or from multiple R processes to exploit parallelism. A wide choice
of finalizer options allows to work with 'permanent' files as well as
creating/removing 'temporary' ff files completely transparent to the user.
On certain OS/Filesystem combinations, creating the ff files works without
notable delay thanks to using sparse file allocation. Several access
optimization techniques such as Hybrid Index Preprocessing and
Virtualization are implemented to achieve good performance even with large
datasets, for example virtual matrix transpose without touching a single
byte on disk. Further, to reduce disk I/O, 'logicals' and non-standard
data types get stored native and compact on binary flat files i.e.
logicals take up exactly 2 bits to represent TRUE, FALSE and NA. Beyond
basic access functions, the ff package also provides compatibility
functions that facilitate writing code for ff and ram objects and support
for batch processing on ff objects (e.g. as.ram, as.ff, ffapply). ff
interfaces closely with functionality from package 'bit': chunked looping,
fast bit operations and coercions between different objects that can store
subscript information ('bit', 'bitwhich', ff 'boolean', ri range index, hi
hybrid index). This allows to work interactively with selections of large
datasets and quickly modify selection criteria. Further high-performance
enhancements can be made available upon request.

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
%{rlibdir}/%{packname}/ANNOUNCEMENT*
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/README_devel.txt
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 2.2.13-1
- initial package for Fedora
