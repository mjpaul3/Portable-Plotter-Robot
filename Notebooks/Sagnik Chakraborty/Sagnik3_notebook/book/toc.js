// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="entry_1.html"><strong aria-hidden="true">1.</strong> Entry 1 - Week of 9/16/24</a></li><li class="chapter-item expanded "><a href="entry_2.html"><strong aria-hidden="true">2.</strong> Entry 2 - Week of 9/23/24</a></li><li class="chapter-item expanded "><a href="entry_3.html"><strong aria-hidden="true">3.</strong> Entry 3 - Week of 9/30/24</a></li><li class="chapter-item expanded "><a href="entry_4.html"><strong aria-hidden="true">4.</strong> Entry 4 - Week of 10/07/24</a></li><li class="chapter-item expanded "><a href="entry_5.html"><strong aria-hidden="true">5.</strong> Entry 5 - Week of 10/14/24</a></li><li class="chapter-item expanded "><a href="entry_6.html"><strong aria-hidden="true">6.</strong> Entry 6 - Week of 10/21/24</a></li><li class="chapter-item expanded "><a href="entry_7.html"><strong aria-hidden="true">7.</strong> Entry 7 - Week of 10/28/24</a></li><li class="chapter-item expanded "><a href="entry_8.html"><strong aria-hidden="true">8.</strong> Entry 8 - Week of 11/04/24</a></li><li class="chapter-item expanded "><a href="entry_9.html"><strong aria-hidden="true">9.</strong> Entry 9 - Week of 11/11/24</a></li><li class="chapter-item expanded "><a href="entry_10.html"><strong aria-hidden="true">10.</strong> Entry 10 - Week of 11/18/24</a></li><li class="chapter-item expanded "><a href="entry_11.html"><strong aria-hidden="true">11.</strong> Entry 11 - Week of 11/25/24</a></li><li class="chapter-item expanded "><a href="entry_12.html"><strong aria-hidden="true">12.</strong> Entry 12 - Week of 12/02/24</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString();
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
