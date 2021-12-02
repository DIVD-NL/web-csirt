---
layout: default
title: frontpage
description: DIVD
---
<!-- Highlights -->
<header class="special">
    <h2>our mission</h2>
    <p>We aim to make the digital world safer by reporting vulnerabilities we find in digital systems to the people who can fix them. We have a global reach, but do it Dutch style: open, honest, collaborative and for free.</p>
    <h2>Our statistics</h2>
    {% include stats.html %}
</header>
<div class="highlights">
    <section>
        <div class="content">
            <header>
                <a href="/team" class="icon fa-vcard-o"><span class="label">Icon</span></a>
                <h3>Team</h3>
            </header>
            <p>DIVD is a platform for security researchers to report vulnerabilities, supported by volunteers.</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/code" class="icon fa-balance-scale"><span class="label">Icon</span></a>
                <h3>Code of Conduct</h3>
            </header>
            <p>How and why we scan and report.</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/news" class="icon fa-calendar-o"><span class="label">Icon</span></a>
                <h3>News & Events</h3>
            </header>
            <p>Just getting started with some presentations here and there</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/reports" class="icon fa-files-o"><span class="label">Icon</span></a>
                <h3>REPORTS</h3>
            </header>
            <p>Reports on closed research</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="https://www.securitymeldpunt.nl" class="icon fa-bell-o"><span class="label">Icon</span></a>
                <h3>CSIRT</h3>
            </header>
            <p>Blog on current research by our Computer Security Incident Response Team</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/security" class="icon fa-shield"><span class="label">Icon</span></a>
                <h3>SECURITY</h3>
            </header>
            <p>Public documents and reports about (our) security</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/contact" class="icon fa-envelope-o"><span class="label">Icon</span></a>
                <h3>CONTACT</h3>
            </header>
            <p>We are a network of security researchers who mainly work online.</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/join" class="icon fa-handshake-o"><span class="label">Icon</span></a>
                <h3>JOIN</h3>
            </header>
            <p>Join DIVD</p>
        </div>
    </section>
    <section>
        <div class="content">
            <header>
                <a href="/donate" class="icon fa-eur"><span class="label">Icon</span></a>
                <h3>DONATE</h3>
            </header>
            <p>We need your support for our mission.</p>
        </div>
    </section>
</div>

{% include open-cases.html %}
{% include last-10-posts.html %}