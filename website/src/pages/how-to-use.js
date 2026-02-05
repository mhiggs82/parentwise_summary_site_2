import React from 'react';
import Layout from '@theme/Layout';

export default function HowToUse() {
    return (
        <Layout title="How to Use ParentWise" description="Your journey to confident parenting begins here. Master the wisdom of experts in minutes.">
            <main style={{ backgroundColor: 'var(--pw-bg-canvas)', color: 'white', minHeight: '100vh', fontFamily: "'Lexend', sans-serif", paddingBottom: '80px' }}>

                {/* Hero Section */}
                <section style={{ maxWidth: '960px', margin: '0 auto', padding: '80px 24px', textAlign: 'center' }}>
                    <h1 style={{ fontSize: '48px', fontWeight: '900', marginBottom: '24px', trackingTight: '-0.02em', lineHeight: '1.1' }}>
                        Getting Started
                    </h1>
                    <p style={{ color: 'var(--pw-text-secondary)', fontSize: '20px', fontWeight: '300', maxWidth: '672px', margin: '0 auto', lineHeight: '1.6' }}>
                        Your journey to confident parenting begins here. Master the wisdom of experts in minutes with our focused summaries and action plans.
                    </p>
                </section>

                {/* Quick Start Steps */}
                <section style={{ maxWidth: '1080px', margin: '0 auto', padding: '0 24px 96px' }}>
                    <div style={{ textAlign: 'center', marginBottom: '48px' }}>
                        <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '8px' }}>Quick Start Steps</h2>
                        <div style={{ height: '4px', width: '48px', backgroundColor: 'var(--pw-purple)', borderRadius: '999px', margin: '0 auto' }}></div>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '48px', position: 'relative' }}>
                        {/* Step 1 */}
                        <StepCard number="1" icon="explore" title="Explore" description="Browse our curated library of top parenting bestsellers tailored to your needs." />
                        {/* Step 2 */}
                        <StepCard number="2" icon="menu_book" title="Read" description="Digest key insights and expert strategies in under 15 minutes per book." />
                        {/* Step 3 */}
                        <StepCard number="3" icon="task_alt" title="Apply" description="Use our 'Action' tabs to turn abstract advice into immediate daily habits." />
                    </div>
                </section>

                {/* Platform Highlights */}
                <section style={{ maxWidth: '1080px', margin: '0 auto', padding: '0 24px 96px' }}>
                    <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '40px', textAlign: 'center' }}>Platform Highlights</h2>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px' }}>
                        <HighlightCard
                            icon="search"
                            title="Smart Search"
                            description="Don't just search for titles. Search for problems like 'tantrums' or 'sleep regression' to find specific advice instantly."
                        />
                        <HighlightCard
                            icon="filter_list"
                            title="Category Filters"
                            description="Zero in on what matters. Filter content tailored specifically to Toddlers, Teens, Single Parents, and everyone in between."
                        />
                        <HighlightCard
                            icon="view_column"
                            title="Dual-Tab Cards"
                            description="Every summary has two modes: 'Deep Analysis' for understanding the why, and 'Action Plan' for executing the how."
                        />
                    </div>
                </section>

                {/* Sanctuary Box (Tips) */}
                <section style={{ maxWidth: '800px', margin: '0 auto', padding: '0 24px 96px' }}>
                    <div style={{
                        backgroundColor: 'rgba(26, 29, 46, 0.6)',
                        border: '1px solid rgba(111, 92, 255, 0.3)',
                        borderRadius: '16px',
                        padding: '40px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '32px',
                        boxShadow: '0 0 20px rgba(111, 92, 255, 0.15)'
                    }}>
                        <div style={{ display: 'flex', gap: '32px', alignItems: 'flex-start' }}>
                            <div style={{ flexShrink: 0 }}>
                                <div style={{ width: '56px', height: '56px', backgroundColor: 'rgba(111, 92, 255, 0.2)', borderRadius: '50%', display: 'flex', alignItems: 'center', justify: 'center', border: '1px solid rgba(111, 92, 255, 0.3)', color: 'var(--pw-purple)' }}>
                                    <span className="material-symbols-outlined" style={{ fontSize: '30px', margin: 'auto' }}>lightbulb</span>
                                </div>
                            </div>
                            <div>
                                <h3 style={{ fontSize: '20px', fontWeight: '700', marginBottom: '16px' }}>Sanctuary Tip: Choosing Your First Read</h3>
                                <ul style={{ listStyle: 'none', padding: 0, display: 'flex', flexDirection: 'column', gap: '16px' }}>
                                    <li style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
                                        <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '20px' }}>check_circle</span>
                                        <span style={{ color: 'rgba(255,255,255,0.8)', fontSize: '14px', lineHeight: '1.6' }}>
                                            <strong style={{ color: 'white' }}>Urgent Fixes:</strong> Look for the "Immediate Action" tag if you are dealing with an acute behavioral issue right now.
                                        </span>
                                    </li>
                                    <li style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
                                        <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '20px' }}>check_circle</span>
                                        <span style={{ color: 'rgba(255,255,255,0.8)', fontSize: '14px', lineHeight: '1.6' }}>
                                            <strong style={{ color: 'white' }}>Long-term Growth:</strong> Select "Developmental Foundations" for books that build character and long-term resilience.
                                        </span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>

                {/* CTA Footer */}
                <section style={{ maxWidth: '960px', margin: '0 auto', padding: '0 24px 48px', textAlign: 'center' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '24px' }}>
                        <button className="pw-button" style={{
                            height: '64px',
                            fontSize: '18px',
                            padding: '0 48px',
                            borderRadius: '16px'
                        }}>
                            Go to Homepage
                        </button>
                        <a href="/docs/parenting" style={{ color: 'var(--pw-text-secondary)', fontSize: '14px', fontWeight: '500', textDecoration: 'underline', textUnderlineOffset: '4px' }}>
                            Or browse all categories
                        </a>
                    </div>
                </section>

            </main>
        </Layout>
    );
}

function StepCard({ number, icon, title, description }) {
    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
            <div style={{
                width: '80px',
                height: '80px',
                borderRadius: '24px',
                backgroundColor: 'var(--pw-bg-card)',
                border: '1px solid #352e6b',
                boxShadow: '0 0 20px rgba(111, 92, 255, 0.15)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                marginBottom: '24px',
                position: 'relative'
            }}>
                <span style={{
                    position: 'absolute',
                    top: '-12px',
                    right: '-12px',
                    width: '32px',
                    height: '32px',
                    backgroundColor: 'var(--pw-purple)',
                    borderRadius: '50%',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '14px',
                    fontWeight: '700',
                    boxShadow: '0 4px 6px rgba(0,0,0,0.3)'
                }}>{number}</span>
                <span className="material-symbols-outlined" style={{ fontSize: '36px' }}>{icon}</span>
            </div>
            <h3 style={{ fontSize: '20px', fontWeight: '700', marginBottom: '8px' }}>{title}</h3>
            <p style={{ color: 'var(--pw-text-secondary)', fontSize: '14px', lineHeight: '1.6', maxWidth: '240px' }}>{description}</p>
        </div>
    );
}

function HighlightCard({ icon, title, description }) {
    return (
        <div style={{
            backgroundColor: 'var(--pw-bg-card)',
            border: '1px solid #2a264a',
            borderRadius: '16px',
            padding: '32px',
            display: 'flex',
            flexDirection: 'column',
            height: '100%'
        }}>
            <div style={{
                marginBottom: '20px',
                padding: '12px',
                backgroundColor: '#25204b',
                width: 'fit-content',
                borderRadius: '12px',
                color: '#7c5bff'
            }}>
                <span className="material-symbols-outlined" style={{ fontSize: '28px' }}>{icon}</span>
            </div>
            <h3 style={{ fontSize: '18px', fontWeight: '700', marginBottom: '12px' }}>{title}</h3>
            <p style={{ color: 'var(--pw-text-secondary)', fontSize: '14px', lineHeight: '1.6', flexGrow: 1 }}>{description}</p>
        </div>
    );
}
