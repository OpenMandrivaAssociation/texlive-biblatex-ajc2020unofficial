Name:		texlive-biblatex-ajc2020unofficial
Version:	54401
Release:	2
Summary:	BibLaTeX style for the Australasian Journal of Combinatorics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-ajc2020unofficial
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an unofficial BibLaTeX style for the Australasian
Journal of Combinatorics. Note that the journal (as for 01
March 2020) does not accept BibLaTeX, so you probably want to
use biblatex2bibitem.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-ajc2020unofficial
%doc %{_texmfdistdir}/doc/latex/biblatex-ajc2020unofficial

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
