import React from 'react';
import Layout from '@theme/Layout';

export default function About() {
    return (
        <Layout title="About ParentWise" description="Navigating the noise of modern parenting with scientific precision and human empathy.">
            <main style={{ backgroundColor: 'var(--pw-bg-canvas)', color: 'white', minHeight: '100vh', fontFamily: "'Lexend', sans-serif" }}>

                {/* Header Section */}
                <section style={{ maxWidth: '1280px', margin: '0 auto', padding: '80px 24px 48px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <div style={{
                        marginBottom: '24px',
                        width: '64px',
                        height: '64px',
                        borderRadius: '50%',
                        backgroundColor: 'rgba(124, 91, 255, 0.1)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        border: '1px solid rgba(124, 91, 255, 0.2)',
                        boxShadow: '0 0 20px rgba(124, 91, 255, 0.15)'
                    }}>
                        <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '36px' }}>local_florist</span>
                    </div>
                    <h1 style={{ fontSize: '36px', fontWeight: '700', lineHeight: '1.2', marginBottom: '16px', letterSpacing: '-0.02em' }}>About ParentWise</h1>
                    <p style={{ color: 'var(--pw-text-secondary)', fontSize: '18px', maxWidth: '672px', margin: '0 auto', fontWeight: '300', lineHeight: '1.6' }}>
                        Navigating the noise of modern parenting with scientific precision and human empathy.
                    </p>
                </section>

                {/* Mission Section */}
                <section style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 24px 96px' }}>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '48px', alignItems: 'center' }}>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
                            <p style={{ fontSize: '18px', lineHeight: '1.6', color: 'rgba(255,255,255,0.8)' }}>
                                ParentWise was born from a simple observation: parents are overwhelmed with information but starved for wisdom. We exist to filter the noise, curating only the most scientifically validated advice for your journey.
                            </p>
                            <p style={{ fontSize: '18px', lineHeight: '1.6', color: 'rgba(255,255,255,0.8)' }}>
                                We don't just aggregate data; we synthesize it. By bridging the gap between academic journals and the daily breakfast table, we turn anxiety into confidence.
                            </p>
                        </div>

                        {/* Sanctuary Box */}
                        <div style={{
                            backgroundColor: 'var(--pw-bg-card)',
                            borderRadius: '24px',
                            padding: '40px',
                            border: '1px solid rgba(46, 58, 107, 0.4)',
                            position: 'relative',
                            overflow: 'hidden'
                        }}>
                            <div style={{ position: 'absolute', top: 0, right: 0, width: '256px', height: '256px', backgroundColor: 'rgba(124, 91, 255, 0.05)', borderRadius: '50%', filter: 'blur(100px)', marginRight: '-80px', marginTop: '-80px', pointerEvents: 'none' }}></div>
                            <div style={{ position: 'relative', zIndex: 1, display: 'flex', flexDirection: 'column', gap: '24px' }}>
                                <h3 style={{ color: 'var(--pw-purple)', fontWeight: '700', letterSpacing: '0.1em', textTransform: 'uppercase', fontSize: '12px' }}>Our Mission</h3>
                                <h2 style={{ fontSize: '28px', fontWeight: '700', lineHeight: '1.3' }}>
                                    "To empower every parent with research-backed confidence, transforming complex science into a sanctuary of actionable understanding."
                                </h2>
                                <div style={{ height: '4px', width: '80px', backgroundColor: 'rgba(124, 91, 255, 0.5)', borderRadius: '999px', marginTop: '8px' }}></div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Methodology Grid */}
                <section style={{ maxWidth: '1280px', margin: '0 auto', padding: '48px 24px 80px' }}>
                    <div style={{ marginBottom: '48px' }}>
                        <h2 style={{ fontSize: '30px', fontWeight: '700', marginBottom: '8px' }}>Our Methodology</h2>
                        <p style={{ color: 'var(--pw-text-secondary)', fontSize: '18px' }}>How we transform complex studies into parenting wisdom.</p>
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px' }}>
                        <MethodologyCard
                            icon="verified"
                            title="Expert Curation"
                            description="We partner with top child psychologists and neuroscientists to filter thousands of papers, selecting only high-impact, peer-reviewed research relevant to today's challenges."
                        />
                        <MethodologyCard
                            icon="science"
                            title="The Distillation"
                            description="Complex data is processed through our rigourous synthesis framework, condensing 40-page studies into 5-minute actionable insights without losing scientific nuance."
                        />
                        <MethodologyCard
                            icon="favorite"
                            title="Empathetic Design"
                            description="We craft content that respects your cognitive load. Every summary is delivered in a calm, ad-free environment designed to reduce anxiety, not spike it."
                        />
                    </div>
                </section>

                {/* Meet Sophia Section */}
                <section style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 24px 96px' }}>
                    <div style={{
                        position: 'relative',
                        background: 'linear-gradient(to right, var(--pw-bg-card), #161927)',
                        borderRadius: '24px',
                        padding: '48px',
                        overflow: 'hidden',
                        border: '1px solid rgba(46, 58, 107, 0.4)'
                    }}>
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '48px', alignItems: 'center', position: 'relative', zIndex: 1 }}>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
                                <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '4px 12px', borderRadius: '999px', backgroundColor: 'rgba(124, 91, 255, 0.1)', border: '1px solid rgba(124, 91, 255, 0.3)', width: 'fit-content' }}>
                                    <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '14px' }}>auto_awesome</span>
                                    <span style={{ color: 'var(--pw-purple)', fontSize: '12px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Meet Sophia</span>
                                </div>
                                <h2 style={{ fontSize: '32px', fontWeight: '700', lineHeight: '1.2' }}>
                                    Intelligence Amplified. <br />
                                    <span style={{ color: 'var(--pw-purple)', textShadow: '0 0 15px rgba(124, 91, 255, 0.4)' }}>Wisdom Preserved.</span>
                                </h2>
                                <p style={{ fontSize: '18px', color: 'rgba(255,255,255,0.8)', lineHeight: '1.6' }}>
                                    Sophia is our proprietary intelligence engine. She scans global research databases 24/7, flagging potential breakthroughs.
                                </p>
                                <p style={{ color: 'var(--pw-text-secondary)', lineHeight: '1.6' }}>
                                    However, Sophia doesn't publish. She prepares the groundwork for our human experts, ensuring that while our efficiency is AI-assisted, our wisdom remains distinctly human.
                                </p>
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                                {/* Glowing Logo Visualization */}
                                <div style={{ position: 'relative', width: '256px', height: '256px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                                    <div style={{ position: 'absolute', inset: 0, backgroundColor: 'rgba(124, 91, 255, 0.2)', borderRadius: '50%', filter: 'blur(60px)' }}></div>
                                    <div style={{
                                        position: 'relative',
                                        width: '192px',
                                        height: '192px',
                                        backgroundColor: '#0f1116',
                                        border: '1px solid rgba(124, 91, 255, 0.3)',
                                        borderRadius: '50%',
                                        display: 'flex',
                                        alignItems: 'center',
                                        justifyContent: 'center',
                                        boxShadow: '0 0 30px rgba(124, 91, 255, 0.3)'
                                    }}>
                                        <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '80px' }}>psychology</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* CTA Section */}
                <section style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 24px 96px', textAlign: 'center' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '32px', backgroundColor: '#131621', borderRadius: '24px', padding: '64px', border: '1px solid rgba(46, 58, 107, 0.2)' }}>
                        <h2 style={{ fontSize: '32px', fontWeight: '700' }}>Ready to clarify your journey?</h2>
                        <p style={{ color: 'var(--pw-text-secondary)', fontSize: '18px', maxWidth: '512px' }}>Join thousands of parents who have traded endless scrolling for confident decision making.</p>
                        <button className="pw-button" style={{
                            height: '56px',
                            fontSize: '18px',
                            padding: '0 40px',
                            borderRadius: '16px'
                        }}>
                            <span>Start Exploring</span>
                            <span className="material-symbols-outlined">arrow_forward</span>
                        </button>
                    </div>
                </section>

            </main>
        </Layout>
    );
}

function MethodologyCard({ icon, title, description }) {
    return (
        <div className="pw-card" style={{ display: 'flex', flexDirection: 'column', gap: '20px', padding: '32px' }}>
            <div style={{
                width: '48px',
                height: '48px',
                borderRadius: '12px',
                backgroundColor: '#252a40',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--pw-purple)',
                transition: 'all 0.3s ease'
            }}>
                <span className="material-symbols-outlined" style={{ fontSize: '24px' }}>{icon}</span>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                <h3 style={{ fontSize: '20px', fontWeight: '700', color: 'white' }}>{title}</h3>
                <p style={{ color: 'var(--pw-text-secondary)', lineHeight: '1.6', fontSize: '14px' }}>{description}</p>
            </div>
        </div>
    );
}
