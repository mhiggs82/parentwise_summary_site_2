import React from 'react';
import Layout from '@theme/Layout';

export default function Contact() {
    return (
        <Layout title="Contact & Support" description="Get in touch with ParentWise">
            <main className="container" style={{ paddingTop: '80px', paddingBottom: '120px' }}>

                <div style={{ maxWidth: '900px', margin: '0 auto' }}>
                    <header style={{ textAlign: 'center', marginBottom: '64px' }}>
                        <h1 style={{ fontSize: '36px', fontWeight: '700', marginBottom: '16px' }}>Contact & Support</h1>
                        <p className="text-secondary" style={{ fontSize: '18px' }}>
                            Have questions about a guide? Want to suggest a book? We're here to help.
                        </p>
                    </header>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '48px' }}>
                        {/* Contact Form */}
                        <div className="pw-card">
                            <h2 style={{ fontSize: '24px', marginBottom: '24px' }}>Send a Message</h2>
                            <form>
                                <div style={{ marginBottom: '20px' }}>
                                    <label style={{ display: 'block', marginBottom: '8px', fontSize: '14px', fontWeight: '600' }}>Name</label>
                                    <input type="text" style={{
                                        width: '100%',
                                        background: 'var(--pw-bg-canvas)',
                                        border: '1px solid var(--pw-border)',
                                        borderRadius: '8px',
                                        padding: '12px',
                                        color: 'white'
                                    }} placeholder="Your name" />
                                </div>
                                <div style={{ marginBottom: '20px' }}>
                                    <label style={{ display: 'block', marginBottom: '8px', fontSize: '14px', fontWeight: '600' }}>Email</label>
                                    <input type="email" style={{
                                        width: '100%',
                                        background: 'var(--pw-bg-canvas)',
                                        border: '1px solid var(--pw-border)',
                                        borderRadius: '8px',
                                        padding: '12px',
                                        color: 'white'
                                    }} placeholder="your@email.com" />
                                </div>
                                <div style={{ marginBottom: '24px' }}>
                                    <label style={{ display: 'block', marginBottom: '8px', fontSize: '14px', fontWeight: '600' }}>Message</label>
                                    <textarea rows="5" style={{
                                        width: '100%',
                                        background: 'var(--pw-bg-canvas)',
                                        border: '1px solid var(--pw-border)',
                                        borderRadius: '8px',
                                        padding: '12px',
                                        color: 'white'
                                    }} placeholder="How can we help?"></textarea>
                                </div>
                                <button type="submit" className="pw-button" style={{ width: '100%', justifyContent: 'center' }}>Send Message</button>
                            </form>
                        </div>

                        {/* Support Info & FAQ */}
                        <div>
                            <section style={{ marginBottom: '40px' }}>
                                <h3 style={{ fontSize: '20px', marginBottom: '16px' }}>Frequently Asked Questions</h3>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                                    <div>
                                        <h4 style={{ fontSize: '16px', fontWeight: '600', color: 'var(--pw-purple)', marginBottom: '4px' }}>How often is the library updated?</h4>
                                        <p className="text-secondary" style={{ fontSize: '14px' }}>We add 2-3 new high-fidelity summaries every week based on community suggestions.</p>
                                    </div>
                                    <div>
                                        <h4 style={{ fontSize: '16px', fontWeight: '600', color: 'var(--pw-purple)', marginBottom: '4px' }}>Can I request a specific book?</h4>
                                        <p className="text-secondary" style={{ fontSize: '14px' }}>Yes! Use the form to your left or email us at suggestions@parentwise.com.</p>
                                    </div>
                                </div>
                            </section>

                            <section className="pw-card" style={{ background: 'rgba(124, 91, 255, 0.05)', borderColor: 'var(--pw-purple)' }}>
                                <h3 style={{ fontSize: '18px', marginBottom: '12px' }}>Book Suggestion?</h3>
                                <p className="text-secondary" style={{ fontSize: '14px', marginBottom: '16px' }}>
                                    Tell us which parenting book changed your life, and we'll prioritize it for a summary.
                                </p>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--pw-purple)', fontWeight: '600' }}>
                                    <span>Suggest a Book →</span>
                                </div>
                            </section>
                        </div>
                    </div>
                </div>

            </main>
        </Layout>
    );
}
