<!-- source: https://ui.nuxt.com/components/chat-message --> # ChatMessagePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/ChatMessage.vue)

Display a chat message with icon, avatar, and actions.

## Usage

The ChatMessage component renders an `<article>` element for a `user` or
`assistant` chat message.

![](https://github.com/benjamincanac.png)

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

[](/components/chat-messages)Use the [`ChatMessages`](/components/chat-
messages) component to display a list of chat messages.

### Content

Use the `content` prop to display the message content.

content

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

    
    
    <template>
      <UChatMessage content="Hello! Tell me more about building AI chatbots with Nuxt UI Pro." />
    </template>
    

### Side

Use the `side` prop to display the message on the left or right.

side

right

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

    
    
    <template>
      <UChatMessage
        side="right"
        content="Hello! Tell me more about building AI chatbots with Nuxt UI Pro."
      />
    </template>
    

When using the [`ChatMessages`](/components/chat-messages) component, the
`side` prop is set to `left` for `assistant` messages and `right` for `user`
messages.

### Variant

Use the `variant` prop to change style of the message.

variant

soft

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

    
    
    <template>
      <UChatMessage
        variant="soft"
        content="Hello! Tell me more about building AI chatbots with Nuxt UI Pro."
      />
    </template>
    

When using the [`ChatMessages`](/components/chat-messages) component, the
`variant` prop is set to `naked` for `assistant` messages and `soft` for
`user` messages.

### Icon

Use the `icon` prop to display an [Icon](/components/icon) component next to
the message.

icon

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

    
    
    <template>
      <UChatMessage
        icon="i-lucide-user"
        variant="soft"
        side="right"
        content="Hello! Tell me more about building AI chatbots with Nuxt UI Pro."
      />
    </template>
    

### Avatar

Use the `avatar` prop to display an [Avatar](/components/avatar) component
next to the message.

avatar.src

![](https://github.com/benjamincanac.png)

Hello! Tell me more about building AI chatbots with Nuxt UI Pro.

    
    
    <template>
      <UChatMessage
        :avatar="{
          src: 'https://github.com/benjamincanac.png'
        }"
        variant="soft"
        side="right"
        content="Hello! Tell me more about building AI chatbots with Nuxt UI Pro."
      />
    </template>
    

You can also use the `avatar.icon` prop to display an icon as the avatar.

avatar.icon

Nuxt UI Pro offers several features for building AI chatbots including the
ChatMessage, ChatMessages, and ChatPrompt components. Best practices include
using the useChat composable from Vercel AI SDK, implementing proper message
styling with variants, and utilizing the built-in actions for message
interactions. The components are fully customizable with theming support and
responsive design.

    
    
    <template>
      <UChatMessage
        :avatar="{
          icon: 'i-lucide-bot'
        }"
        content="Nuxt UI Pro offers several features for building AI chatbots including the ChatMessage, ChatMessages, and ChatPrompt components. Best practices include using the useChat composable from Vercel AI SDK, implementing proper message styling with variants, and utilizing the built-in actions for message interactions. The components are fully customizable with theming support and responsive design."
      />
    </template>
    

### Actions

Use the `actions` prop to display actions below the message that will be
displayed when hovering over the message.

Nuxt UI Pro offers several features for building AI chatbots including the
ChatMessage, ChatMessages, and ChatPrompt components. Best practices include
using the useChat composable from Vercel AI SDK, implementing proper message
styling with variants, and utilizing the built-in actions for message
interactions. The components are fully customizable with theming support and
responsive design.

    
    
    <script setup lang="ts">
    const actions = ref([
      {
        label: 'Copy to clipboard',
        icon: 'i-lucide-copy'
      }
    ])
    </script>
    
    <template>
      <UChatMessage
        :actions="actions"
        content="Nuxt UI Pro offers several features for building AI chatbots including the ChatMessage, ChatMessages, and ChatPrompt components. Best practices include using the useChat composable from Vercel AI SDK, implementing proper message styling with variants, and utilizing the built-in actions for message interactions. The components are fully customizable with theming support and responsive design."
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'article'`| `any`  
`content`| | `string`Text content of the message. Use parts when possible.  
`id`| | `string`A unique identifier for the message.  
`role`| | `"data" | "user" | "system" | "assistant"`The 'data' role is deprecated.  
`icon`| | ` string`  
`variant`| `'naked'`| ` "solid" | "outline" | "soft" | "subtle" | "naked"`  
`avatar`| | ` AvatarProps & { [key: string]: any; }`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`side`| `'left'`| ` "right" | "left"`  
`data`| | ` null | string | number | false | true | { [value: string]: JSONValue; } | JSONValue[]`For data messages.  
`actions`| | ` (Omit<ButtonProps, "onClick"> & { onClick?: ((e: MouseEvent, message: Message) => void) | undefined; })[]`Display a list of actions under the message. The `label` will be used in a tooltip. `{ size: 'xs', color: 'neutral', variant: 'ghost' }`Show properties

  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `label?: string`
  * `trailingIcon?: string`Display an icon on the right side.
  * `disabled?: boolean`
  * `class?: any`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `block?: boolean`Render the button full width.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state

  
`compact`| `false`| `boolean`Render the message in a compact style. This is
done automatically when used inside a `UChatPalette`.  
`createdAt`| | ` Date`The timestamp of the message.  
`reasoning`| | ` string`Reasoning for the message.  
`experimental_attachments`| | ` Attachment[]`Additional attachments to be sent along with the message.Show properties

  * `name?: string`The name of the attachment, usually the file name.
  * `contentType?: string`A string indicating the [media type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type). By default, it's extracted from the pathname's extension.
  * `url: string`The URL of the attachment. It can either be a URL to a hosted file or a [Data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs).

  
`annotations`| | ` JSONValue[]`Additional message-specific information added on the server via StreamData  
`toolInvocations`| | ` ToolInvocation[]`Tool invocations (that can be tool calls or tool results, depending on whether or not the invocation has finished) that the assistant made as part of this message.Show properties

  * `state: "partial-call"`
  * `step?: number`
  * `toolCallId: string`ID of the tool call. This ID is used to match the tool call with the tool result.
  * `toolName: string`Name of the tool that is being called.
  * `args: any`Arguments of the tool call. This is a JSON-serializable object that matches the tool's input schema.
  * `state: "call"`
  * `step?: number`
  * `toolCallId: string`ID of the tool call. This ID is used to match the tool call with the tool result.
  * `toolName: string`Name of the tool that is being called.
  * `args: any`Arguments of the tool call. This is a JSON-serializable object that matches the tool's input schema.
  * `state: "result"`
  * `step?: number`
  * `toolCallId: string`ID of the tool call. This ID is used to match the tool call with the tool result.
  * `toolName: string`Name of the tool that is being called.
  * `args: any`Arguments of the tool call. This is a JSON-serializable object that matches the tool's input schema.
  * `result: any`Result of the tool call. This is the result of the tool's execution.

  
`parts`| | ` (TextUIPart | ReasoningUIPart | ToolInvocationUIPart | SourceUIPart | FileUIPart | StepStartUIPart)[]`The parts of the message. Use this for rendering the message in the UI.Assistant messages can have text, reasoning and tool invocation parts. User messages can have text parts.Show properties

  * `type: "text"`
  * `text: string`The text content.
  * `type: "reasoning"`
  * `reasoning: string`The reasoning text.
  * `details: ({ type: "text"; text: string; signature?: string | undefined; } | { type: "redacted"; data: string; })[]`
  * `type: "tool-invocation"`
  * `toolInvocation: ToolInvocation`The tool invocation.
  * `type: "source"`
  * `source: LanguageModelV1Source`The source.
  * `type: "file"`
  * `mimeType: string`
  * `data: string`
  * `type: "step-start"`

  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; content?: ClassNameValue; actions?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{ avatar: (AvatarProps & { [key: string]: any; }) | undefined; }`  
`content`| `{ content: string; }`  
`actions`| `{ actions: (Omit<ButtonProps, "onClick"> & { onClick?: ((e: MouseEvent, message: Message) => void) | undefined; })[] | undefined; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        chatMessage: {
          slots: {
            root: 'group/message relative w-full',
            container: 'relative flex items-start group-data-[role=user]/message:max-w-[75%]',
            leading: 'inline-flex items-center justify-center min-h-6',
            leadingIcon: 'shrink-0',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            content: 'relative text-pretty',
            actions: [
              'opacity-0 group-hover/message:opacity-100 absolute bottom-0 flex items-center',
              'transition-opacity'
            ]
          },
          variants: {
            variant: {
              solid: {
                content: 'bg-inverted text-inverted'
              },
              outline: {
                content: 'bg-default ring ring-default'
              },
              soft: {
                content: 'bg-elevated/50'
              },
              subtle: {
                content: 'bg-elevated/50 ring ring-default'
              },
              naked: {
                content: ''
              }
            },
            side: {
              left: {
                container: 'rtl:justify-end'
              },
              right: {
                container: 'ltr:justify-end ms-auto'
              }
            },
            leading: {
              true: ''
            },
            actions: {
              true: ''
            },
            compact: {
              true: {
                root: 'scroll-mt-3',
                container: 'gap-1.5 pb-3',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs'
              },
              false: {
                root: 'scroll-mt-4 sm:scroll-mt-6',
                container: 'gap-3 pb-8',
                leadingIcon: 'size-8',
                leadingAvatarSize: 'md'
              }
            }
          },
          compoundVariants: [
            {
              compact: true,
              actions: true,
              class: {
                container: 'pb-8'
              }
            },
            {
              leading: true,
              compact: false,
              side: 'left',
              class: {
                actions: 'left-11'
              }
            },
            {
              leading: true,
              compact: true,
              side: 'left',
              class: {
                actions: 'left-6.5'
              }
            },
            {
              variant: [
                'solid',
                'outline',
                'soft',
                'subtle'
              ],
              compact: false,
              class: {
                content: 'px-4 py-3 rounded-lg min-h-12',
                leading: 'mt-2'
              }
            },
            {
              variant: [
                'solid',
                'outline',
                'soft',
                'subtle'
              ],
              compact: true,
              class: {
                content: 'px-2 py-1 rounded-lg min-h-8',
                leading: 'mt-1'
              }
            }
          ],
          defaultVariants: {
            variant: 'naked'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            chatMessage: {
              slots: {
                root: 'group/message relative w-full',
                container: 'relative flex items-start group-data-[role=user]/message:max-w-[75%]',
                leading: 'inline-flex items-center justify-center min-h-6',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                content: 'relative text-pretty',
                actions: [
                  'opacity-0 group-hover/message:opacity-100 absolute bottom-0 flex items-center',
                  'transition-opacity'
                ]
              },
              variants: {
                variant: {
                  solid: {
                    content: 'bg-inverted text-inverted'
                  },
                  outline: {
                    content: 'bg-default ring ring-default'
                  },
                  soft: {
                    content: 'bg-elevated/50'
                  },
                  subtle: {
                    content: 'bg-elevated/50 ring ring-default'
                  },
                  naked: {
                    content: ''
                  }
                },
                side: {
                  left: {
                    container: 'rtl:justify-end'
                  },
                  right: {
                    container: 'ltr:justify-end ms-auto'
                  }
                },
                leading: {
                  true: ''
                },
                actions: {
                  true: ''
                },
                compact: {
                  true: {
                    root: 'scroll-mt-3',
                    container: 'gap-1.5 pb-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  false: {
                    root: 'scroll-mt-4 sm:scroll-mt-6',
                    container: 'gap-3 pb-8',
                    leadingIcon: 'size-8',
                    leadingAvatarSize: 'md'
                  }
                }
              },
              compoundVariants: [
                {
                  compact: true,
                  actions: true,
                  class: {
                    container: 'pb-8'
                  }
                },
                {
                  leading: true,
                  compact: false,
                  side: 'left',
                  class: {
                    actions: 'left-11'
                  }
                },
                {
                  leading: true,
                  compact: true,
                  side: 'left',
                  class: {
                    actions: 'left-6.5'
                  }
                },
                {
                  variant: [
                    'solid',
                    'outline',
                    'soft',
                    'subtle'
                  ],
                  compact: false,
                  class: {
                    content: 'px-4 py-3 rounded-lg min-h-12',
                    leading: 'mt-2'
                  }
                },
                {
                  variant: [
                    'solid',
                    'outline',
                    'soft',
                    'subtle'
                  ],
                  compact: true,
                  class: {
                    content: 'px-2 py-1 rounded-lg min-h-8',
                    leading: 'mt-1'
                  }
                }
              ],
              defaultVariants: {
                variant: 'naked'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            chatMessage: {
              slots: {
                root: 'group/message relative w-full',
                container: 'relative flex items-start group-data-[role=user]/message:max-w-[75%]',
                leading: 'inline-flex items-center justify-center min-h-6',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                content: 'relative text-pretty',
                actions: [
                  'opacity-0 group-hover/message:opacity-100 absolute bottom-0 flex items-center',
                  'transition-opacity'
                ]
              },
              variants: {
                variant: {
                  solid: {
                    content: 'bg-inverted text-inverted'
                  },
                  outline: {
                    content: 'bg-default ring ring-default'
                  },
                  soft: {
                    content: 'bg-elevated/50'
                  },
                  subtle: {
                    content: 'bg-elevated/50 ring ring-default'
                  },
                  naked: {
                    content: ''
                  }
                },
                side: {
                  left: {
                    container: 'rtl:justify-end'
                  },
                  right: {
                    container: 'ltr:justify-end ms-auto'
                  }
                },
                leading: {
                  true: ''
                },
                actions: {
                  true: ''
                },
                compact: {
                  true: {
                    root: 'scroll-mt-3',
                    container: 'gap-1.5 pb-3',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  false: {
                    root: 'scroll-mt-4 sm:scroll-mt-6',
                    container: 'gap-3 pb-8',
                    leadingIcon: 'size-8',
                    leadingAvatarSize: 'md'
                  }
                }
              },
              compoundVariants: [
                {
                  compact: true,
                  actions: true,
                  class: {
                    container: 'pb-8'
                  }
                },
                {
                  leading: true,
                  compact: false,
                  side: 'left',
                  class: {
                    actions: 'left-11'
                  }
                },
                {
                  leading: true,
                  compact: true,
                  side: 'left',
                  class: {
                    actions: 'left-6.5'
                  }
                },
                {
                  variant: [
                    'solid',
                    'outline',
                    'soft',
                    'subtle'
                  ],
                  compact: false,
                  class: {
                    content: 'px-4 py-3 rounded-lg min-h-12',
                    leading: 'mt-2'
                  }
                },
                {
                  variant: [
                    'solid',
                    'outline',
                    'soft',
                    'subtle'
                  ],
                  compact: true,
                  class: {
                    content: 'px-2 py-1 rounded-lg min-h-8',
                    leading: 'mt-1'
                  }
                }
              ],
              defaultVariants: {
                variant: 'naked'
              }
            }
          }
        })
      ]
    })
    

Expand code

[CarouselA carousel with motion and swipe built using
Embla.](/components/carousel)[ChatMessagesDisplay a list of chat messages,
designed to work seamlessly with Vercel AI SDK.](/components/chat-messages)

