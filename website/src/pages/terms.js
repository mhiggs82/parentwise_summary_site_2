import React from 'react';
import Layout from '@theme/Layout';

export default function Terms() {
    return (
        <Layout title="Terms of Service" description="Terms and conditions for using the ParentWise platform.">
            <main style={{ backgroundColor: 'var(--pw-bg-canvas)', color: 'white', minHeight: '100vh', fontFamily: "'Lexend', sans-serif", padding: '80px 24px' }}>
                <div style={{ maxWidth: '800px', margin: '0 auto' }}>
                    <h1 style={{ fontSize: '48px', fontWeight: '900', marginBottom: '40px', textAlign: 'center' }}>Terms of Service</h1>

                    <div style={{ backgroundColor: 'var(--pw-bg-card)', padding: '40px', borderRadius: '24px', border: '1px solid var(--pw-border)', lineHeight: '1.6' }}>
                        <p style={{ color: 'var(--pw-text-secondary)', marginBottom: '32px' }}>Last Updated: February 5, 2026</p>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>1. Acceptance of Terms</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                By accessing or using ParentWise ("the Platform"), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our services.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>2. Educational Disclaimer</h2>
                            <div style={{ borderLeft: '4px solid var(--pw-purple)', paddingLeft: '20px', margin: '20px 0', backgroundColor: 'rgba(124, 91, 255, 0.05)', padding: '20px', borderRadius: '0 12px 12px 0' }}>
                                <p style={{ fontWeight: '600', marginBottom: '10px' }}>NOT MEDICAL ADVICE</p>
                                <p style={{ fontSize: '14px', color: 'rgba(255,255,255,0.8)' }}>
                                    The content on ParentWise, including book summaries, research distillations, and action plans, is for informational and educational purposes only. It is not intended to be a substitute for professional medical, psychological, or psychiatric advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition or behavioral health concerns.
                                </p>
                            </div>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>3. Use of Sophia (AI Assistance)</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                ParentWise utilizes proprietary AI technology ("Sophia") to assist in the research and synthesis of information. While we strive for accuracy, AI-generated insights are always reviewed by human experts before publication. However, no synthesis is exhaustive, and users should exercise their own judgment.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>4. Intellectual Property</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                All content, including but not limited to summary text, action frameworks, and design elements, is the property of ParentWise. You may use the content for personal, non-commercial use only. Redistribution or commercial use without express written consent is strictly prohibited.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>5. Subscription and Billing</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                Access to certain features may require a paid subscription. All fees are non-refundable except as required by law. You are responsible for maintaining the confidentiality of your account credentials.
                            </p>
                        </section>

                        <section style={{ marginBottom: '32px' }}>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>6. Limitation of Liability</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                ParentWise shall not be liable for any indirect, incidental, special, or consequential damages resulting from your use of the Platform or the application of advice contained within our summaries.
                            </p>
                        </section>

                        <section>
                            <h2 style={{ fontSize: '24px', fontWeight: '700', marginBottom: '16px', color: 'var(--pw-purple)' }}>7. Contact</h2>
                            <p style={{ color: 'rgba(255,255,255,0.8)' }}>
                                For questions regarding these terms, please contact us at support@parentwise.com.
                            </p>
                        </section>
                    </div>
                </div>
            </main>
        </Layout>
    );
}
