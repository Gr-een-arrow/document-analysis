// app/doc-analyzer/page.tsx
"use client";

import { useEffect, useRef, useState } from 'react';
import feather from 'feather-icons';
import 'aos/dist/aos.css';
import AOS from 'aos';

export default function DocAnalyzerPage() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  // Removed dragActive state
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    AOS.init();
    feather.replace();
  }, []);

  // Auto-resize textarea
  const handleInput = () => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = "auto";
      textarea.style.height = textarea.scrollHeight + "px";
    }
  };

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <div
        className={`sidebar bg-white w-64 border-r border-gray-200 flex flex-col md:relative absolute z-10 transition-all duration-300 ${
          sidebarOpen ? "open" : ""
        }`}
      >
        <div className="p-4 border-b border-gray-200 flex justify-between items-center">
          <h1 className="text-xl font-bold text-[#6C63FF]">DocAnalyzer AI</h1>
          <button className="md:hidden" onClick={() => setSidebarOpen(false)}>
            <i data-feather="x"></i>
          </button>
        </div>

        <div className="p-4">
          <button className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-4 rounded-lg flex items-center justify-center gap-2 transition">
            <i data-feather="plus"></i>
            <span>New Chat</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto px-2">
          <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider px-2 mb-2">
            Recent Chats
          </h3>
          <div className="space-y-1">
            {[
              {
                title: "Quarterly Financial Report Analysis",
                time: "2 hours ago",
              },
              { title: "Legal Contract Review", time: "Yesterday", active: true },
              { title: "Research Paper Summary", time: "3 days ago" },
              { title: "Product Requirements Doc", time: "1 week ago" },
            ].map((chat, i) => (
              <div
                key={i}
                className={`group flex items-center justify-between p-2 rounded-lg cursor-pointer transition ${
                  chat.active
                    ? "bg-indigo-50"
                    : "hover:bg-gray-100"
                }`}
              >
                <div className="flex-1 min-w-0">
                  <p
                    className={`text-sm font-medium truncate ${
                      chat.active ? "text-indigo-900" : "text-gray-900"
                    }`}
                  >
                    {chat.title}
                  </p>
                  <p
                    className={`text-xs truncate ${
                      chat.active ? "text-indigo-700" : "text-gray-500"
                    }`}
                  >
                    {chat.time}
                  </p>
                </div>
                <div className="flex items-center opacity-0 group-hover:opacity-100 transition">
                  <button className="p-1 text-gray-400 hover:text-indigo-600">
                    <i data-feather="edit-2" className="w-4 h-4"></i>
                  </button>
                  <button className="p-1 text-gray-400 hover:text-red-600">
                    <i data-feather="trash-2" className="w-4 h-4"></i>
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="p-4 border-t border-gray-200 flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center">
            <i data-feather="user" className="text-indigo-600 w-4 h-4"></i>
          </div>
          <div>
            <p className="text-sm font-medium">John Doe</p>
            <p className="text-xs text-gray-500">john@example.com</p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        {/* Top Bar */}
        <div className="bg-white border-b border-gray-200 p-4 flex items-center justify-between">
          <button className="md:hidden" onClick={() => setSidebarOpen(true)}>
            <i data-feather="menu"></i>
          </button>
          <h2 className="text-lg font-semibold text-gray-900">
            Legal Contract Review
          </h2>

        </div>

        {/* Document Cards */}
        <div className="bg-gray-50 border-b border-gray-200 p-4 overflow-x-auto">
          <div className="flex gap-3">
            {[
              { name: "Contract_v1.pdf", size: "PDF • 2.4MB", color: "indigo" },
              {
                name: "NDA_Agreement.docx",
                size: "DOCX • 1.1MB",
                color: "green",
              },
              {
                name: "Terms_of_Service.pdf",
                size: "PDF • 3.2MB",
                color: "blue",
              },
            ].map((doc, i) => (
              <div
                key={i}
                className="document-card flex-shrink-0 bg-white rounded-lg border border-gray-200 p-2 w-32 flex flex-col items-center hover:shadow-md"
              >
                <div
                  className={`w-8 h-8 bg-${doc.color}-100 rounded-full flex items-center justify-center mb-1`}
                >
                  <i
                    data-feather="file-text"
                    className={`text-${doc.color}-600`}
                  ></i>
                </div>
                <p className="text-sm font-medium text-center truncate w-full text-gray-900">
                  {doc.name}
                </p>
                <p className="text-xs text-gray-600">{doc.size}</p>
              </div>
            ))}

            <button className="flex-shrink-0 bg-white rounded-lg border-2 border-dashed border-gray-300 p-3 w-40 flex flex-col items-center justify-center hover:border-indigo-300 hover:bg-indigo-50 transition">
              <div className="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center mb-2">
                <i data-feather="plus" className="text-gray-500"></i>
              </div>
              <p className="text-sm font-medium text-center text-gray-600">
                Add Document
              </p>
            </button>
          </div>
        </div>

        {/* Drag & Drop Area removed */}

        {/* Chat Messages */}
        <div className="chat-container overflow-y-auto p-4 flex-1 bg-white">
          <div className="max-w-3xl mx-auto space-y-4">
            {/* AI Message */}
            <div className="flex gap-3">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                <i data-feather="cpu" className="text-green-600 w-4 h-4"></i>
              </div>
              <div className="message-ai p-4 max-w-[80%] bg-white shadow rounded-lg">
                <p className="text-sm text-gray-900">
                  I&#39;ve analyzed the three documents you uploaded. Here&#39;s a
                  summary:
                </p>
                <ul className="list-disc pl-5 mt-2 text-sm space-y-1 text-gray-900">
                  <li>
                    <span className="font-medium">Contract_v1.pdf</span>: 15
                    clauses, 3 areas needing legal review
                  </li>
                  <li>
                    <span className="font-medium">NDA_Agreement.docx</span>:
                    2-year term with penalties
                  </li>
                  <li>
                    <span className="font-medium">Terms_of_Service.pdf</span>:
                    Auto-renewal clause
                  </li>
                </ul>
              </div>
            </div>

            {/* User Message */}
            <div className="flex justify-end gap-3">
              <div className="message-user p-4 max-w-[80%] bg-indigo-600 text-white rounded-lg">
                <p className="text-sm text-white">
                  Can you highlight the most unusual clause in
                  Contract_v1.pdf?
                </p>
              </div>
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-indigo-100 flex items-center justify-center">
                <i data-feather="user" className="text-indigo-600 w-4 h-4"></i>
              </div>
            </div>

            {/* AI Response */}
            <div className="flex gap-3">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                <i data-feather="cpu" className="text-green-600 w-4 h-4"></i>
              </div>
              <div className="message-ai p-4 max-w-[80%] bg-white shadow rounded-lg">
                <p className="text-sm text-gray-900">
                  The most unusual clause in Contract_v1.pdf is Section 4.3:
                </p>
                <div className="bg-indigo-50 p-3 rounded-md mt-2 text-sm">
                  <p className="font-medium text-[#6C63FF]">
                    &quot;In the event of termination, the Client shall be liable for
                    150% of remaining contract value.&quot;
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Input Area */}
        <div className="border-t border-gray-200 p-4 bg-white">
          <div className="max-w-3xl mx-auto">
            <div className="relative">
              <textarea
                ref={textareaRef}
                className="w-full border border-gray-300 rounded-lg pl-4 pr-12 py-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 resize-none"
                rows={1}
                placeholder="Ask about your documents..."
                style={{ minHeight: "44px", maxHeight: "120px" }}
                onInput={handleInput}
                // Removed dragActive handlers
              />
              <div className="absolute right-3 bottom-3 flex gap-1">
                <button className="p-1 text-gray-400 hover:text-indigo-600">
                  <i data-feather="paperclip" className="w-5 h-5"></i>
                </button>
                <button className="p-1 text-gray-400 hover:text-indigo-600">
                  <i data-feather="mic" className="w-5 h-5"></i>
                </button>
                <button className="p-1 bg-indigo-600 text-white rounded-lg p-2 hover:bg-indigo-700 transition">
                  <i data-feather="send" className="w-5 h-5"></i>
                </button>
              </div>
            </div>
            <p className="text-xs text-indigo-700 mt-2">
              DocAnalyzer AI may produce inaccurate information. Verify details.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
