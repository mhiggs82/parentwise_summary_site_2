import React from 'react';
import Layout from '@theme/Layout';
import clsx from 'clsx';

export default function Newsletter() {
    return (
        <Layout title="Wisdom Well" description="Weekly Parenting Wisdom, Distilled.">
            <main style={{
                backgroundColor: 'var(--pw-bg-canvas)',
                minHeight: '100vh',
                padding: '64px 24px',
                fontFamily: "'Lexend', sans-serif"
            }}>
                <div style={{ maxWidth: '1024px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '80px' }}>

                    {/* Hero Section */}
                    <section style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '24px' }}>
                        <div style={{ position: 'relative', width: '64px', height: '64px' }}>
                            <div style={{
                                position: 'absolute',
                                inset: 0,
                                backgroundColor: 'var(--pw-purple)',
                                borderRadius: '50%',
                                filter: 'blur(20px)',
                                opacity: 0.2
                            }}></div>
                            <div style={{
                                position: 'relative',
                                width: '64px',
                                height: '64px',
                                borderRadius: '16px',
                                background: 'linear-gradient(135deg, var(--pw-bg-card), #252a40)',
                                border: '1px solid #2a2f45',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                boxShadow: '0 0 10px rgba(124, 92, 255, 0.3)'
                            }}>
                                <span className="material-symbols-outlined" style={{ color: 'var(--pw-purple)', fontSize: '32px' }}>eco</span>
                            </div>
                        </div>

                        <div style={{ maxWidth: '672px' }}>
                            <h1 style={{
                                fontSize: '48px',
                                fontWeight: '900',
                                lineHeight: '1.1',
                                letterSpacing: '-0.02em',
                                background: 'linear-gradient(to bottom, #fff, rgba(255,255,255,0.7))',
                                WebkitBackgroundClip: 'text',
                                WebkitTextFillColor: 'transparent',
                                marginBottom: '16px'
                            }}>
                                Wisdom Well:<br />Weekly Insights, Distilled.
                            </h1>
                            <p style={{ fontSize: '18px', color: 'var(--pw-text-secondary)', fontWeight: '300' }}>
                                Join <span style={{ color: 'white', fontWeight: '500' }}>5,000+ parents</span> getting science-backed wisdom delivered to their inbox every Tuesday.
                            </p>
                        </div>
                    </section>

                    {/* Value Stack Grid */}
                    <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '24px' }}>
                        <FeatureCard
                            icon="auto_stories"
                            title="New Summaries"
                            description="Complex academic studies turned into 5-minute easy reads for busy parents."
                        />
                        <FeatureCard
                            icon="psychology"
                            title="Research Deep-Dives"
                            description="Understand the 'Why' behind the advice with clear, evidence-based explanations."
                        />
                        <FeatureCard
                            icon="checklist"
                            title="Exclusive Actions"
                            description="Practical, actionable steps you can implement in your daily routine immediately."
                        />
                    </section>

                    {/* Subscription Card */}
                    <section style={{ maxWidth: '512px', margin: '0 auto', width: '100%' }}>
                        <div style={{
                            position: 'relative',
                            borderRadius: '24px',
                            padding: '1px',
                            background: 'linear-gradient(to bottom, #3a2e6b, var(--pw-bg-card))',
                            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)'
                        }}>
                            <div style={{
                                position: 'relative',
                                backgroundColor: 'var(--pw-bg-card)',
                                borderRadius: '23px',
                                padding: '40px'
                            }}>
                                <div style={{ textAlign: 'center', marginBottom: '32px' }}>
                                    <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '8px' }}>Join the Inner Circle</h2>
                                    <p style={{ color: 'var(--pw-text-secondary)', fontSize: '14px' }}>Get the next issue this coming Tuesday.</p>
                                </div>

                                <form style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                                    <div style={{ position: 'relative' }}>
                                        <span className="material-symbols-outlined" style={{
                                            position: 'absolute',
                                            left: '16px',
                                            top: '50%',
                                            transform: 'translateY(-50%)',
                                            color: 'var(--pw-text-tertiary)',
                                            fontSize: '20px'
                                        }}>person</span>
                                        <input
                                            type="text"
                                            placeholder="First Name"
                                            style={{
                                                width: '100%',
                                                height: '56px',
                                                paddingLeft: '48px',
                                                paddingRight: '16px',
                                                backgroundColor: 'var(--pw-bg-canvas)',
                                                border: '1px solid #2a2f45',
                                                borderRadius: '12px',
                                                color: 'white',
                                                outline: 'none'
                                            }}
                                        />
                                    </div>

                                    <div style={{ position: 'relative' }}>
                                        <span className="material-symbols-outlined" style={{
                                            position: 'absolute',
                                            left: '16px',
                                            top: '50%',
                                            transform: 'translateY(-50%)',
                                            color: 'var(--pw-text-tertiary)',
                                            fontSize: '20px'
                                        }}>mail</span>
                                        <input
                                            type="email"
                                            placeholder="Email Address"
                                            style={{
                                                width: '100%',
                                                height: '56px',
                                                paddingLeft: '48px',
                                                paddingRight: '16px',
                                                backgroundColor: 'var(--pw-bg-canvas)',
                                                border: '1px solid #2a2f45',
                                                borderRadius: '12px',
                                                color: 'white',
                                                outline: 'none'
                                            }}
                                        />
                                    </div>

                                    <button className="pw-button" style={{
                                        height: '56px',
                                        justifyContent: 'center',
                                        fontSize: '16px',
                                        marginTop: '8px',
                                        width: '100%'
                                    }}>
                                        Subscribe to the Sanctuary
                                        <span className="material-symbols-outlined">arrow_forward</span>
                                    </button>
                                </form>

                                <p style={{ textAlign: 'center', fontSize: '12px', color: 'var(--pw-text-tertiary)', marginTop: '24px', fontWeight: '500' }}>
                                    No spam. Just science. Unsubscribe anytime.
                                </p>
                            </div>
                        </div>
                    </section>

                    {/* Testimonial */}
                    <section style={{ textAlign: 'center', maxWidth: '672px', margin: '0 auto', padding: '0 16px' }}>
                        <div style={{ color: 'rgba(124, 91, 255, 0.4)', marginBottom: '16px' }}>
                            <span className="material-symbols-outlined" style={{ fontSize: '40px' }}>format_quote</span>
                        </div>
                        <blockquote style={{
                            fontSize: '24px',
                            fontWeight: '500',
                            color: 'var(--pw-text-secondary)',
                            lineHeight: '1.6',
                            margin: '0 0 24px 0',
                            fontStyle: 'italic'
                        }}>
                            "Finally, parenting advice that respects my intelligence and doesn't rely on fear-mongering."
                        </blockquote>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                            <span style={{ color: 'white', fontWeight: '700', fontSize: '16px' }}>Sarah Jenkins</span>
                            <span style={{ color: 'var(--pw-text-tertiary)', fontSize: '14px' }}>Mom of 2, Subscriber since 2022</span>
                        </div>
                    </section>

                </div>
            </main>
        </Layout>
    );
}

function FeatureCard({ icon, title, description }) {
    return (
        <div className="pw-card" style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '24px' }}>
            <div style={{
                width: '48px',
                height: '48px',
                borderRadius: '12px',
                backgroundColor: 'rgba(124, 91, 255, 0.1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--pw-purple)',
                transition: 'all 0.3s ease'
            }}>
                <span className="material-symbols-outlined">{icon}</span>
            </div>
            <div>
                <h3 style={{ fontSize: '18px', fontWeight: '700', marginBottom: '8px', color: 'white' }}>{title}</h3>
                <p style={{ fontSize: '14px', color: 'var(--pw-text-secondary)', lineHeight: '1.6' }}>{description}</p>
            </div>
        </div>
    );
}
