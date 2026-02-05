import React from 'react';
import Layout from '@theme/Layout';

export default function Privacy() {
    return (
        <Layout title="Privacy Policy" description="How ParentWise collects and protects your data.">
            <main style={{ backgroundColor: 'var(--pw-bg-canvas)', color: 'white', minHeight: '100vh', fontFamily: "'Lexend', sans-serif", padding: '80px 24px' }}>
                <div style={{ maxWidth: '800px', margin: '0 auto' }}>
                    <h1 style={{ fontSize: '48px', fontWeight: '900', marginBottom: '40px', textAlign: 'center' }}>Privacy Policy</h1>

                    <div style={{ backgroundColor: 'var(--pw-bg-card)', padding: '40px', borderRadius: '24px', border: '1px solid var(--pw-border)', lineHeight: '1.6' }}>
                        <p style={{ color: 'var(--pw-text-secondary)', marginBottom: '32px' }}>Last Updated: February 5, 2026</p>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>1. Information We Collect</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)', marginBottom: '16px' }}>
                                We collect information to provide better services to our users. This includes:
                            </p>
                            <ul style={{ color: 'rgba(255,255,255,0.8)', paddingLeft: '20px' }}>
                                <li style={{ marginBottom: '8px' }}><strong style={{ color: 'white' }}>Personal Information:</strong> Name and email address when you sign up for our newsletter ("Wisdom Well") or create an account.</li>
                                <li style={{ marginBottom: '8px' }}><strong style={{ color: 'white' }}>Usage Data:</strong> Information on how you interact with our library, which summaries you view, and your search queries.</li>
                                <li style={{ marginBottom: '8px' }}><strong style={{ color: 'white' }}>Payment Information:</strong> Processed through secure third-party providers (like Stripe); we do not store full credit card details.</li>
                            </ul>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>2. How We Use Information</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                We use the information to deliver summaries, personalize your library experience, process payments, and send the Wisdom Well newsletter. We also use aggregated, non-identifying data to improve the Platform.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>3. Data Sharing</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                We do not sell your personal data to third parties. We only share information with service providers (e.g., email hosting, payment processing) as necessary to operate the Platform.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>4. Cookies and Tracking</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                We use cookies to maintain your session and understand site usage. You can disable cookies in your browser settings, though some features of the Platform may not function correctly.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>5. Your Rights</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                You have the right to access, correct, or delete your personal information. You can unsubscribe from our newsletter at any time by clicking the link at the bottom of any email.
                            </p>
                        </section>

                        <section>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>6. Security</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                We implement industry-standard security measures to protect your data, but no method of transmission over the internet is 100% secure.
                            </p>
                        </section>
                    </div>
                </div>
            </main>
        </Layout>
    );
}
