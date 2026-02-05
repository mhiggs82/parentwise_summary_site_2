import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import Translate from '@docusaurus/Translate';

export default function NotFound() {
    return (
        <Layout
            title="Page Not Found"
            description="Page Not Found">
            <main className="flex-grow flex flex-col items-center justify-center p-4 sm:p-8 relative overflow-hidden min-h-[calc(100vh-300px)]">
                {/* Background Ambient Glow */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-[#7c5bff]/5 rounded-full blur-[100px] -z-10 pointer-events-none"></div>

                <div className="max-w-[800px] w-full flex flex-col items-center text-center gap-8 z-10">
                    {/* Icon Section */}
                    <div className="relative group">
                        <div className="absolute inset-0 bg-[#7c5bff]/20 rounded-full blur-xl group-hover:bg-[#7c5bff]/30 transition-all duration-700"></div>
                        <span className="material-symbols-outlined text-[#7c5bff] text-[80px] sm:text-[100px] relative z-10 leaf-glow opacity-90" style={{ fontSize: '100px' }}>spa</span>
                    </div>

                    {/* Text Content */}
                    <div className="space-y-4 max-w-xl">
                        <h1 className="text-3xl sm:text-4xl font-bold tracking-tight text-slate-900 dark:text-white leading-tight">
                            Oops! This page is lost in translation.
                        </h1>
                        <p className="text-slate-600 dark:text-[#9a8dce] text-base sm:text-lg font-light leading-relaxed">
                            Even the best parents get turned around sometimes. Let's get you back on track to finding the wisdom you need.
                        </p>
                    </div>

                    {/* Recovery Grid */}
                    <div className="w-full bg-white dark:bg-[#1a1d2e] rounded-xl sm:rounded-2xl p-6 sm:p-8 shadow-xl shadow-slate-200/50 dark:shadow-none border border-slate-100 dark:border-white/5 mt-4">
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
                            {/* Column 1: Top Categories */}
                            <div className="flex flex-col gap-4">
                                <div className="flex items-center gap-2 text-[#7c5bff] font-semibold text-sm uppercase tracking-wider">
                                    <span className="material-symbols-outlined text-lg">category</span>
                                    Top Categories
                                </div>
                                <nav className="flex flex-col gap-3">
                                    <Link to="/docs/foundational" className="text-slate-600 dark:text-slate-300 hover:text-[#7c5bff] dark:hover:text-[#7c5bff] transition-colors text-sm flex items-center justify-between group">
                                        Foundational Books
                                        <span className="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0">chevron_right</span>
                                    </Link>
                                    <Link to="/docs/communication" className="text-slate-600 dark:text-slate-300 hover:text-[#7c5bff] dark:hover:text-[#7c5bff] transition-colors text-sm flex items-center justify-between group">
                                        Communication
                                        <span className="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0">chevron_right</span>
                                    </Link>
                                    <Link to="/docs/teen-development" className="text-slate-600 dark:text-slate-300 hover:text-[#7c5bff] dark:hover:text-[#7c5bff] transition-colors text-sm flex items-center justify-between group">
                                        Teen Development
                                        <span className="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0">chevron_right</span>
                                    </Link>
                                    <Link to="/docs/parent-self-work" className="text-slate-600 dark:text-slate-300 hover:text-[#7c5bff] dark:hover:text-[#7c5bff] transition-colors text-sm flex items-center justify-between group">
                                        Parent Self-work
                                        <span className="material-symbols-outlined text-[16px] opacity-0 group-hover:opacity-100 transition-opacity -translate-x-2 group-hover:translate-x-0">chevron_right</span>
                                    </Link>
                                </nav>
                            </div>

                            {/* Column 2: Quick Search */}
                            <div className="flex flex-col gap-4 md:border-x md:border-slate-100 md:dark:border-white/5 md:px-6">
                                <div className="flex items-center gap-2 text-[#7c5bff] font-semibold text-sm uppercase tracking-wider">
                                    <span className="material-symbols-outlined text-lg">search</span>
                                    Quick Search
                                </div>
                                <p className="text-xs text-slate-500 dark:text-slate-400">Looking for a specific book or topic?</p>
                                <div className="relative w-full group cursor-text">
                                    {/* Search functionality would go here, relying on Docusaurus search */}
                                    <p className="text-sm italic text-slate-400">Please use the site search bar (cmd+k)</p>
                                </div>
                                <Link to="/" className="w-full mt-2 bg-slate-100 dark:bg-white/5 hover:bg-slate-200 dark:hover:bg-white/10 text-slate-700 dark:text-slate-200 text-xs font-medium py-2 px-4 rounded-lg transition-colors text-center">
                                    Go to Homepage
                                </Link>
                            </div>

                            {/* Column 3: Popular Summaries */}
                            <div className="flex flex-col gap-4">
                                <div className="flex items-center gap-2 text-[#7c5bff] font-semibold text-sm uppercase tracking-wider">
                                    <span className="material-symbols-outlined text-lg">trending_up</span>
                                    Popular Now
                                </div>
                                <nav className="flex flex-col gap-3">
                                    <Link to="/docs/foundational/FOUND-003 - The Whole-Brain Child by Daniel Siegel and Tina Payne Bryson" className="group flex items-start gap-3 hover:bg-slate-50 dark:hover:bg-white/5 p-2 rounded-lg -ml-2 transition-colors">
                                        <div className="flex flex-col">
                                            <span className="text-sm font-medium text-slate-800 dark:text-slate-200 group-hover:text-[#7c5bff] transition-colors">The Whole-Brain Child</span>
                                            <span className="text-xs text-slate-500 dark:text-slate-400">Daniel J. Siegel</span>
                                        </div>
                                    </Link>
                                    <Link to="/docs/foundational/FOUND-001 - Good Inside by Becky Kennedy" className="group flex items-start gap-3 hover:bg-slate-50 dark:hover:bg-white/5 p-2 rounded-lg -ml-2 transition-colors">
                                        <div className="flex flex-col">
                                            <span className="text-sm font-medium text-slate-800 dark:text-slate-200 group-hover:text-[#7c5bff] transition-colors">Good Inside</span>
                                            <span className="text-xs text-slate-500 dark:text-slate-400">Becky Kennedy</span>
                                        </div>
                                    </Link>
                                </nav>
                            </div>
                        </div>
                    </div>

                    {/* CTA */}
                    <div className="mt-4">
                        <Link to="/" className="inline-flex items-center justify-center gap-2 bg-[#7c5bff] hover:bg-[#6a4ce6] text-white font-semibold py-4 px-8 rounded-lg shadow-lg shadow-[#7c5bff]/30 hover:shadow-[#7c5bff]/50 transition-all duration-300 transform hover:-translate-y-0.5">
                            <span className="material-symbols-outlined">home</span>
                            Back to Homepage
                        </Link>
                    </div>
                </div>
            </main>
        </Layout>
    );
}
