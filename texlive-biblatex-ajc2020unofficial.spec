%global tl_name biblatex-ajc2020unofficial
%global tl_revision 54401

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.0
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for the Australasian Journal of Combinatorics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-ajc2020unofficial
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ajc2020unofficial.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an unofficial BibLaTeX style for the Australasian Journal of
Combinatorics. Note that the journal (as for 01 March 2020) does not
accept BibLaTeX, so you probably want to use biblatex2bibitem.

